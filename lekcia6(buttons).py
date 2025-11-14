from tkinter import *
from tkinter import messagebox

def forButton(event):
    Window.geometry("650x560")
    Window.config(bg="green") 
    button_widget.config(bg="lightblue")
    
Window = Tk()
Window.geometry("400x300")
Window.title("Вікно №1")
button_widget = Button( Window, text="Розфарбуй",fg="white", bg="red")
button_widget.bind("<Button-1>", forButton)
button_widget.place(x=100, y=100, width=210, height=40) 
Window.mainloop()


def colorBg (event):
    Window2 ["bg"] = "purple"
    button ["bg"] = "yellow"
    messagebox.showinfo("Повідомлення","Завдання виконано!")

Window2 = Tk()
Window2.geometry("500x800")
Window2.title("Вікно №2")
button = Button(Window2, text ="OK", fg = "purple", bg= "light blue")
button.place(x = 200, y = 390)
button.bind("<Button-1>", colorBg)
Window2.mainloop()


def piska(event):
    Window3.geometry("560x435")
    Window3 ["bg"] = "yellow"
    messagebox.showinfo("Виконано","Зміни застосовані!")

Window3 = Tk()
Window3.title("Це вікно Python")
button3 = Button(Window3, text="Змінити", bg = "pink", fg = "light blue")
button3.bind("<Button-3>", piska)
button3.pack(pady=100)
Window3.mainloop()