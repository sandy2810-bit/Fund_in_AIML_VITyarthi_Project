import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        attended = int(entry_attended.get())
        total = int(entry_total.get())

        if total == 0:
            messagebox.showerror("Error", "Total classes cannot be zero")
            return

        attendance = (attended / total) * 100
        result_text.set(f"Attendance: {attendance:.2f}%")

        if attendance < 75:
            needed = 0
            a, t = attended, total
            while (a / t) * 100 < 75:
                a += 1
                t += 1
                needed += 1
            prediction_text.set(f"You need to attend {needed} more classes")
        else:
            bunk = 0
            while (attended / (total + bunk)) * 100 >= 75:
                bunk += 1
            prediction_text.set(f"You can bunk {bunk - 1} classes")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# GUI Window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="Attendance Tracker", font=("Arial", 16, "bold")).pack(pady=10)

# Inputs
tk.Label(root, text="Attended Classes").pack()
entry_attended = tk.Entry(root)
entry_attended.pack()

tk.Label(root, text="Total Classes").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# Button
tk.Button(root, text="Calculate", command=calculate, bg="blue", fg="white").pack(pady=10)

# Results
result_text = tk.StringVar()
prediction_text = tk.StringVar()

tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack()
tk.Label(root, textvariable=prediction_text, font=("Arial", 12)).pack()

root.mainloop()
