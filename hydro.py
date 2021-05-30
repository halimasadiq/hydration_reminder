import tkinter as tk
from tkinter import *
from sys import exit
import time
import threading

class Water:
    def __init__(root):
        super().__init__()

        #configuring the root window
        root = Tk()
        root.title("HydroAssist")
        root.resizable(False,False)
        root.config(bg="#E6f7ff")

        #Positioning the window at the center of the screen
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/3 - windowHeight/3)
        root.geometry("+{}+{}".format(positionRight, positionDown))

        #####################################################
        #heading
        myTitle = Label(root, text="Paani Pi Lo", font=("bold",10), bg="#E6f7ff")
        myTitle.grid(row=0, column=0, columnspan = 3, padx=50, pady=10, sticky='e')

        #reminderText
        reminderText = Label(root, text="Remind me every", bg="#E6f7ff")
        reminderText.grid(row = 2, column =0, padx=(30,0), pady=10)
        reminderMinutes = Label(root, text="minutes", bg="#E6f7ff")
        reminderMinutes.grid(row=2, column=3, padx=(0,30), pady=10)

        #dropdown menu for setting timer
        options = [1,10, 20,30,40,50,60]
        clicked = StringVar()
        clicked.set(1)
        dropdown = OptionMenu(root, clicked, *options)
        dropdown.config(bg="#E6f7ff")
        dropdown["menu"].config(bg="#Bee6f9")
        dropdown.grid(row=2, column = 1, pady=10)

        timerAmount = int(clicked.get())
        timerAmount = timerAmount * 60
        print(timerAmount)

        Button(root, text="Done", command = exit, bg="#E6f7ff").grid(row=4,column=0, pady=20)

        root.after()


    def DrinkWater(self):
        popupRoot = Tk()
        popupRoot.after(2000, exit)
        popupButton = Button(popupRoot, text = "Drink Water", font = ("Verdana", 12), bg = "yellow", command = exit)
        popupButton.pack()
        popupRoot.geometry('400x50+700+500')
        popupRoot.attributes('-alpha',0.5)
        popupRoot.after(50000,self.DrinkWater)
        popupRoot.mainloop()
    

if __name__ == "__main__":
    water = Water()
    water.DrinkWater()
    water.mainloop


