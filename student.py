import tkinter as tk
from tkinter import messagebox
import database

database.connect()

def refresh_list():
    listbox.delete(0, tk.END)
    for row in database.fetch_all():
        listbox.insert(tk.END, row)

def on_select(event):
    selected = listbox.get(listbox.curselection())
    id_var.set(selected[0])
    name_var.set(selected[1])
    age_var.set(selected[2])
    course_var.set(selected[3])

def add():
    if name_var.get() and age_var.get() and course_var.get():
        database.insert(name_var.get(), int(age_var.get()), course_var.get())
        refresh_list()
        clear()
    else:
        messagebox.showwarning("Input Error", "Fill all fields.")

def update():
    try:
        if id_var.get() and name_var.get() and age_var.get() and course_var.get():
            database.update(int(id_var.get()), name_var.get(), int(age_var.get()), course_var.get())
            refresh_list()
            clear()
        else:
            messagebox.showwarning("Input Error", "Fill all fields.")
    except ValueError:
        messagebox.showerror("Error", "Invalid age or ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def delete():
    if id_var.get():
        database.delete(int(id_var.get()))
        refresh_list()
        clear()

def search():
    listbox.delete(0, tk.END)
    for row in database.search(name_var.get()):
        listbox.insert(tk.END, row)

def clear():
    id_var.set("")
    name_var.set("")
    age_var.set("")
    course_var.set("")

root = tk.Tk()
root.title("Advanced Student Management")

id_var = tk.StringVar()
name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)

tk.Label(root, text="Course").grid(row=2, column=0)
tk.Entry(root, textvariable=course_var).grid(row=2, column=1)

tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Update", command=update).grid(row=3, column=1)
tk.Button(root, text="Delete", command=delete).grid(row=3, column=2)
tk.Button(root, text="Search", command=search).grid(row=4, column=0)
tk.Button(root, text="Clear", command=clear).grid(row=4, column=1)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=5, column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", on_select)

refresh_list()
root.mainloop()
