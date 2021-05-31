from tkinter import *
from sys import exit
import time
import threading
import sys
from PIL import Image,ImageTk

print(sys.getrecursionlimit())

def DrinkWater(time_given):
    popupRoot = Toplevel()
    #Positioning the window at the center of the screen
    window_Width = popupRoot.winfo_reqwidth()
    window_Height = popupRoot.winfo_reqheight()
    position_Right = int(popupRoot.winfo_screenwidth()/2 - window_Width/2)
    position_Down = int(popupRoot.winfo_screenheight()/3 - window_Height/3)
    popupRoot.geometry("+{}+{}".format(position_Right, position_Down))
    #adding backgroung image to DrinkWater popup
    bg = ImageTk.PhotoImage(Image.open("backw.jpg"))
    #Label1 = Label(popupRoot, image = bg)
    #Label1.pack()
    popupButton = Label(popupRoot, text = "Drink Water", font = ("Verdana", 40), image = bg)
    popupButton.pack()
    popupRoot.attributes('-alpha',0.5)
    popupRoot.attributes('-topmost',True)  
    popupRoot.after(2000,popupRoot.destroy)
    root.after(time_given,lambda: DrinkWater(time_given))
    popupRoot.mainloop()


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
selected = IntVar(root)
selected.set(1)
dropdown = OptionMenu(root, selected, *options)
dropdown.config(bg="#E6f7ff")
dropdown["menu"].config(bg="#Bee6f9")
dropdown.grid(row=2, column = 1, pady=10)

def time_Selected():
    print(selected.get())
    return selected.get()
timeSelected = (selected.get() * 60 *1000)
#timeSelected = 5000

def printTime():
    print(timeSelected)


#change exit to drinkwater
Button(root, text="Done Selecting", command = time_Selected, bg="#E6f7ff").grid(row=4,column=1, pady=20)
Button(root, text="Close the program", command = exit, bg="#E6f7ff").grid(row=5,column=1, pady=20)

def run():
    DrinkWater(timeSelected)
    root.after(2000,run)

#root.after(2000,run)
DrinkWater(timeSelected)
root.mainloop()

