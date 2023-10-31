import tkinter as tk
from tkinter import messagebox
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            winsound.Beep(500, 1000)
            messagebox.showinfo("Alarm", "Time to wake up!")
            break

app = tk.Tk()
app.title("Alarm Clock")

label = tk.Label(app, text="Enter the alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(app)
entry.pack()

set_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_button.pack()

app.mainloop()
