from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()
window.title("Clock")
window.geometry("540x230")
window.iconbitmap("icon.ico")


time_label = Label(window,font=("Inter",70),fg="#F8F8F8",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",33,"bold"))
day_label.pack()

date_label = Label(window,font=("Shelvia Montanila",33))
date_label.pack()

update()

window.mainloop()