from tkinter import *

#lekcia 5
Window1 = Tk()
Window1.title("Вікно №1")
Window1.geometry("1650x1080")
Window1 ["bg"] = "green"
Window1 = mainloop()
#lekcia 5.1 
Window2 = Tk()
Window2.title("Це вікно!")
Window2.geometry("400x400")
Window2.minsize("100x100")
Window2 ["bg"] = "orange"
Window2 = mainloop()
#lekcia 5.2
Window3 = Tk()
Window3.geometry("100x500")
Window3.title("Яйко")
Window3.resizable(False, False)
Window3 ["bg"] = "white"
Window3 = mainloop()
#lekcia 5.3
Window4 = Tk()
Window4.geometry("654x456+300+400")
Window4 ["bg"] = "yellow"
Window4.resizable(False, False)
Window4.title("Вікно №4")
Window4 = mainloop()
#lekcia 5.4 5
Window5 = Tk()
Window5.title("Вікно №5")
Window5.geometry("700x300+100+0")
Window5.config(bg = "light blue")
Window5.resizable(False,False)
Window5.mainloop()
Window6 = Tk()
Window6.title("Вікно №5")
Window6.geometry("700x300+100+0")
Window6.config(bg = "blue")
Window6.resizable(False,False)
Window6.mainloop()

