from tkinter import *
from tkinter import messagebox

def change(event):
    Window.geometry("400x300")
    Window ["bg"] = "green"
    messagebox.showinfo("Повідомлення", "Я програмую на Python")
    Window.title("Rivne")
def Button3(event):
    Window.resizable(False, False)
    Window.geometry("700x600")
    Window ["bg"] = "thistle"
    Window.title ("RCIT")
def KeyPress(event):
    Window.geometry("300x200")
    Window ["bg"] = "yellow"
    Window.title("Gionix")
    Window.minsize("200, 100")
    Window.maxsize("1000, 900")
Window = Tk()
Window.geometry("500x500")
Window ["bg"] = "blue"
Window.bind("<Button-1>", change)
Window.bind("<Button-3>", Button3)
Window.bind("<KeyPress>", KeyPress)
Window.mainloop()
