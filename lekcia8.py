from tkinter import *
Window = Tk()
Window.geometry("500x500")
canv = Canvas(Window, width = 500, height= 500, bg = "light blue")
canv.place(x = 0, y = 0)
canv.create_line([100,100], [200,200], width = 3, fill ="green")
canv.create_rectangle([200, 200], [400, 400], width = 3, fill = "green")
canv.create_oval([200, 200], [400, 400], width = 3, fill = "yellow")
Window.mainloop()
