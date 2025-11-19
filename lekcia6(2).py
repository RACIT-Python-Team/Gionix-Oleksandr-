from tkinter import *
from tkinter import messagebox

def KeyButton(event):
    Window.geometry("500x600")
    Window ["bg"] = "gray"
    Window.title("IPZ2/2")
    Window.minsize("400x500")
    Window.maxsize("900x1000")
def Button2(event):
    messagebox.showinfo("Я навчаюсь в ІПЗ 2/2")
def Button3(event):
    new_window = Toplevel() 
    new_window.geometry("400x300")
    new_window.config(bg="red")
    new_window.title("Вікно №2")
Window = Tk()
Window.geometry("500x500")
Window ["bg"] = "blue"
Window.bind("<Button-1>", Button2)
Window.bind("<KeyPress>", KeyButton)
Window.bind("<Button-3>", Button3)
Window.mainloop()
