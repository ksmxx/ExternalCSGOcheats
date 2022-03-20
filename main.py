import tkinter
from esp import *
from radar import *
from trigger import *
master = tkinter.Tk()
master.title("grid() method")
master.geometry("225x125")
master.title("MattHacks")

button2=tkinter.Button(master, text="ESP", command = esp)
button2.grid(row=1,column=1)

button3=tkinter.Button(master, text="Chams")
button3.grid(row=1,column=2)

button4=tkinter.Button(master, text="Radar", command = radar)
button4.grid(row=2,column=1)

button5=tkinter.Button(master, text="Trigger", command = trigger)
button5.grid(row=2,column=2)

master.mainloop()
