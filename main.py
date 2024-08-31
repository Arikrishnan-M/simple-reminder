import tkinter as tk
from tkinter import messagebox
import time
import threading



def set_reminder():
    reminder_time = entry_time.get()
    reminder_message = entry_message.get()

    try:
        reminder_time_in_seconds = int(reminder_time) * 60
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the time.")
        return

    if reminder_time_in_seconds > 0:

        threading.Thread(target=reminder, args=(reminder_time_in_seconds, reminder_message)).start()



def reminder(reminder_time, reminder_message):
    time.sleep(reminder_time)
    messagebox.showinfo("Reminder", reminder_message)



root = tk.Tk()
root.title("Reminder App")
tk.Label(root, text="Set Reminder Time (in minutes):").pack(pady=10)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

tk.Label(root, text="Reminder Message:").pack(pady=10)
entry_message = tk.Entry(root)
entry_message.pack(pady=5)

tk.Button(root, text="Set Reminder", command=set_reminder).pack(pady=20)


root.mainloop()
