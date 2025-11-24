from tkinter import *
from tkinter import messagebox
Window1 = Tk()

def start (event):
    messagebox.showinfo("Повідомлення",f"Вас звати: {entry1.get()}")
    label= Label(Window1, text = "Привіт світ!", bg = "light blue", fg = "black", font = "Calibri 12")
    label.place(x=30, y=40)
    label["text"] = entry1.get()
but = Button(Window1)
entry1 = Entry(Window1, bg = "Grey", width = 40, font = "Times 15")
entry1.place(x=50, y = 50)
but.place(x=30, y=40)
but.bind("<Button-1>", start)
Window1.mainloop()
