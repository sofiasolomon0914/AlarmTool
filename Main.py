"""
This program will allow user to set an alarm that will go off with a sounds and also allow a message to display while
the alarm is going off.
"""

from tkinter import *
import time


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


root = Tk()
clock = Label(root, font=("times", 100, "bold"), bg="white")
clock.grid(row=0, column=1)
tick()
root.mainloop()
