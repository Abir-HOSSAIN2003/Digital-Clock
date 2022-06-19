import tkinter as ui
import time

window = ui.Tk()

#variable that creates and updates various aspects of the clock such as the hour, minutes, second, and time of day
def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    #A full statement is needed in order to read out the time so the following statement is created
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(500, update_clock)

 #This allows for the ui to be tested as well as adjust the font of the clock
digital_clock_lbl = ui.Label(window, text="00:00:00",
                             font= "Times_New_Roman 72 bold")

digital_clock_lbl.pack()

update_clock()

window.mainloop()