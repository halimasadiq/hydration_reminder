from tkinter import *
import time
 

def update_clock():
    timer_label.config(text=time.strftime('%H:%M:%S',time.localtime()),
                  font='Times 25')  # change the text of the time_label according to the current time
    root.after(100, update_clock)  # reschedule update_clock function to update time_label every 100 ms

root = Tk()  # create the root window
timer_label = Label(root, justify='center')  # create the label for timer
timer_label.pack()  # show the timer_label using pack geometry manager
root.after(0, update_clock)  # schedule update_clock function first call
root.mainloop()  # start the root window mainloop