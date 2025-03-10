import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database Setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL, category TEXT, description TEXT, date TEXT)")
conn.commit()

# Add Expense
def add_expense():
    amount = amount_entry.get()
    category = category_var.get()
    desc = desc_entry.get()
    date = date_entry.get()

    if amount and category and date:
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)", 
                       (amount, category, desc, date))
        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")

# GUI Setup
root = tk.Tk()
root.title("Expense Tracker")

ttk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1)

ttk.Label(root, text="Category:").grid(row=1, column=0)
category_var = tk.StringVar(value="Food")
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Food", "Transport", "Entertainment", "Others"])
category_dropdown.grid(row=1, column=1)

ttk.Label(root, text="Description:").grid(row=2, column=0)
desc_entry = ttk.Entry(root)
desc_entry.grid(row=2, column=1)

ttk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0)
date_entry = ttk.Entry(root)
date_entry.grid(row=3, column=1)

ttk.Button(root, text="Add Expense", command=add_expense).grid(row=4, columnspan=2, pady=10)

root.mainloop()
