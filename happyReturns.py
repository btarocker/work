from tkinter import *
from tkinter import ttk


def insert_employees():
    # Combines first and last name and clears entry fields
    emp_full_name.set(value=f"{emp_first_name.get()} {emp_last_name.get()}")
    current_employees.append(emp_full_name.get())
    emp_first_name.set(value='')
    emp_last_name.set(value='')
    list_employees()

def list_employees():
    third_label.pack()
    print_label.grid(column=0, row=0, padx=10)
    alt_label.grid(column=0, columnspan=2, row=1)

def delete_employees():
    pass

current_employees = []

window = Tk()
window.geometry("350x300")
window.title("Happy Returns Employees")
s = ttk.Style()

# text variables
emp_first_name = StringVar()
emp_last_name = StringVar()
emp_full_name = StringVar()

# main layout areas
first_label = ttk.Label(window)
second_label = ttk.Label(window)
third_label = ttk.Label(window)

# labels

emp_first_label = ttk.Label(first_label, text="Enter Employee first name:")
emp_last_label = ttk.Label(first_label, text="Enter Employee last name:")
alt_label = ttk.Label(third_label, text='Successfully added')
print_label = ttk.Label(third_label, textvariable=emp_full_name)

# entries
emp_first_entry = ttk.Entry(first_label, textvariable=emp_first_name)
emp_last_entry = ttk.Entry(first_label, textvariable=emp_last_name)

# buttons
submit_button = ttk.Button(second_label, text="Submit", command=insert_employees)
quit_button = ttk.Button(second_label, text="Quit", command=quit)

# first label section
first_label.pack()
emp_first_label.grid(column=0, row=0, padx=10, pady=10)
emp_first_entry.grid(column=1, row=0, padx=10, pady=10)
emp_last_label.grid(column=0, row=1, padx=10, pady=10)
emp_last_entry.grid(column=1, row=1, padx=10, pady=10)

# second label section
second_label.pack()
submit_button.grid(column=0, row=1, pady=10)
quit_button.grid(column=1, row=1, pady=10)

window.mainloop()