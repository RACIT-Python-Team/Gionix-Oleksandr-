import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


dots_style = mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
line_style = mp_draw.DrawingSpec(color=(255, 0, 0), thickness=4)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    

    count = 0

    if results.multi_hand_landmarks:

        count = len(results.multi_hand_landmarks)
        
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks( frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, landmark_drawing_spec=dots_style, connection_drawing_spec=line_style )


    cv2.putText(frame, f"Hands: {count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Hands Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()