# Clock Program
from tkinter import *
from time import *

# For complete list of directives check here:
# https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-and-strptime-behavior


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)  # Changed this from time_label to window to update all strings


window = Tk()

time_label = Label(window, font=("Impact", 50), fg="#00FF00", bg="black", width=15)
time_label.pack()

day_label = Label(window, font=("Nirmala UI", 25))
day_label.pack()

date_label = Label(window, font=("Nirmala UI", 30))
date_label.pack()

update()

window.mainloop()
