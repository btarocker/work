import csv
import os.path
from datetime import date
from tkcalendar import DateEntry
from tkinter import *
from customtkinter import *

fields = ['Serial Number', 'Date Check-in', 'Initial Check-in', 'HUB', 'iPad version']
filename = "c:/temp/assets.csv"

def insert_data():
    # Combines first and last name and clears entry fields
    full_data.set(value=f"{model_num.get()} {serial_num.get()}")
    asset_data.update({'iPad version': model_num.get()})
    asset_data.update({"Serial Number": serial_num.get().upper()})
    asset_data.update({"Date Check-in" : date_entry.get_date()})
    asset_data.update({"Initial Check-in" : "EA"})
    asset_data.update({"HUB": "VNC"})
    write_file()

def write_file():
    # Creates and/or appends asset csv file
    if os.path.exists("c:/temp/assets.csv"):
        with open(filename, "a", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fields)
            writer.writerow(asset_data)
        model_num.set(value='')
        serial_num.set(value='')
        list_data()
    else:
        with open(filename, "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fields)
            writer.writeheader()
            writer.writerow(asset_data)
        model_num.set(value='')
        serial_num.set(value='')
        list_data()


# lists data added in window
def list_data():
    third_label.pack()
    print_label.grid(column=0, row=0, padx=10)
    alt_label.grid(column=0, columnspan=2, row=1)

def delete_data():
    pass

asset_data = {"Serial Number": "",  "Date Check-in": "", "Initial Check-in": "", "HUB": "", "iPad version": ""}
ipad_models = ("Mini 4", "Mini 5", "Mini 6", "iPad 9")


window = CTk()
window.geometry("350x300")
window.title("HRAT")

# text variables
model_num = StringVar()
serial_num = StringVar()
full_data = StringVar()

# main layout areas
first_label = CTkLabel(window, text='')
second_label = CTkLabel(window, text='')
third_label = CTkLabel(window, text='')

# labels

model_label = CTkLabel(first_label, text="Enter Model #:")
serial_label = CTkLabel(first_label, text="Enter Serial #:")
date_label = CTkLabel(first_label, text='Enter Date Received:')
print_label = CTkLabel(third_label, textvariable=full_data)
alt_label = CTkLabel(third_label, text='Successfully added')

# entries
model_entry = CTkComboBox(first_label, values=ipad_models, variable=model_num, corner_radius=0, state='readonly')
serial_entry = CTkEntry(first_label, textvariable=serial_num, corner_radius=0)
date_entry = DateEntry(first_label, maxdate=date.today())
serial_entry.bind("<Return>", lambda e: insert_data())

# buttons
submit_button = CTkButton(second_label, text="Submit", width=100, command=insert_data)
quit_button = CTkButton(second_label, text="Quit", width=100, command=quit)

# first label section
first_label.pack()
model_label.grid(column=0, row=0, padx=10, pady=5)
model_entry.grid(column=1, row=0, padx=10, pady=5)
serial_label.grid(column=0, row=1, padx=10, pady=5)
serial_entry.grid(column=1, row=1, padx=10, pady=5)
date_label.grid(column=0, row=2, padx=10, pady=5)
date_entry.grid(column=1, row=2, padx=10, pady=5)

# second label section
second_label.pack()
submit_button.grid(column=0, row=1, pady=10, padx=5)
quit_button.grid(column=1, row=1, pady=10, padx=5)

window.mainloop()