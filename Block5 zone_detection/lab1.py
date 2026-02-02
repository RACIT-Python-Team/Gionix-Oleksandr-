import cv2
import mediapipe as mp
import numpy as np
import os

IMAGE_PATH = "photo.jpg" 
ROI_WIDTH_PERCENT = 0.7
ROI_HEIGHT_PERCENT = 0.8
TOUCH_THRESHOLD_Y_PERCENT = 0.55 
INDEX_FINGER_TIP_ID = 8

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

if os.path.exists(IMAGE_PATH):
    map_image_original = cv2.imread(IMAGE_PATH)
    print(f"Зображення завантажено: {IMAGE_PATH}")
else:
    print(f"УВАГА: Файл {IMAGE_PATH} не знайдено! Створюємо чорний фон.")
    map_image_original = np.zeros((600, 800, 3), dtype=np.uint8)
    cv2.putText(map_image_original, "IMAGE NOT FOUND", (50, 300), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


INTERACTIVE_ZONES = [
    {"name": "Reception", "norm_coords": [0.10, 0.10, 0.45, 0.40], "color": (255, 255, 0)},
    {"name": "Staff Room", "norm_coords": [0.55, 0.10, 0.90, 0.40], "color": (0, 165, 255)},
    {"name": "Exit",       "norm_coords": [0.30, 0.60, 0.70, 0.90], "color": (0, 0, 255)}    
]

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape

    ROI_W = int(W * ROI_WIDTH_PERCENT)
    ROI_H = int(H * ROI_HEIGHT_PERCENT)
    ROI_X_START = int((W - ROI_W) / 2)
    ROI_Y_START = int((H - ROI_H) / 2)
    TOUCH_THRESHOLD_Y_ABS = int(H * TOUCH_THRESHOLD_Y_PERCENT)

    
    resized_map = cv2.resize(map_image_original, (ROI_W, ROI_H), interpolation=cv2.INTER_AREA)

   
    frame[ROI_Y_START : ROI_Y_START + ROI_H, ROI_X_START : ROI_X_START + ROI_W] = resized_map

  
    cv2.line(frame, (0, TOUCH_THRESHOLD_Y_ABS), (W, TOUCH_THRESHOLD_Y_ABS), (0, 255, 255), 2)


    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    detected_zone = None
    finger_color = (0, 255, 0) 
    status_text = "Awaiting Touch"
    
   
    scaled_norm_x, scaled_norm_y = 0.0, 0.0
    abs_x, abs_y = 0, 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            tip = hand_landmarks.landmark[INDEX_FINGER_TIP_ID]
            abs_x, abs_y = int(tip.x * W), int(tip.y * H)

            
            is_touching_y = abs_y < TOUCH_THRESHOLD_Y_ABS
            is_in_roi = (abs_x >= ROI_X_START and abs_x <= ROI_X_START + ROI_W and
                         abs_y >= ROI_Y_START and abs_y <= ROI_Y_START + ROI_H)

            if is_touching_y and is_in_roi:
                finger_color = (255, 255, 255) 
                
            
                relative_x = abs_x - ROI_X_START
                relative_y = abs_y - ROI_Y_START
                scaled_norm_x = relative_x / ROI_W
                scaled_norm_y = relative_y / ROI_H

         
                for zone in INTERACTIVE_ZONES:
                    min_x, min_y, max_x, max_y = zone["norm_coords"]
                    
                    if (scaled_norm_x >= min_x and scaled_norm_x <= max_x and
                        scaled_norm_y >= min_y and scaled_norm_y <= max_y):
                        
                        detected_zone = zone["name"]
                        finger_color = zone["color"] 
                        

                        z_x1 = ROI_X_START + int(min_x * ROI_W)
                        z_y1 = ROI_Y_START + int(min_y * ROI_H)
                        z_x2 = ROI_X_START + int(max_x * ROI_W)
                        z_y2 = ROI_Y_START + int(max_y * ROI_H)
                        

                        cv2.rectangle(frame, (z_x1, z_y1), (z_x2, z_y2), (255, 255, 255), 4)
                        
                        status_text = f"ACTIVE: {detected_zone}"
                        break
                    else:
                        status_text = "ACTIVE: Unmapped Area"

            
            
            cv2.circle(frame, (abs_x, abs_y), 10, finger_color, -1)

           
            if is_touching_y and is_in_roi:
                cv2.putText(frame, f"({scaled_norm_x:.2f}, {scaled_norm_y:.2f})", 
                           (abs_x + 15, abs_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, finger_color, 2)


    text_color = finger_color if detected_zone else (0, 255, 255)
    cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    cv2.imshow('Lab 1: Zone Hit Test', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

hands.close()
cap.release()
cv2.destroyAllWindows()