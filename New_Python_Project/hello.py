import os
import tkinter as tk
import json

# list1 = {}

def file_entry():
    file1 = os.open(f"{user_file.get()}",os.O_RDONLY)
    readfile = os.read(file1, 85).decode("utf-8-sig")
    readfile = readfile.split(sep=',')
    
    list1 = {i: item for i, item in enumerate(readfile, start=1)}
    list1 = json.dumps(list1, indent=4)
    
    label2 = tk.Label(window, text="Headers of this file are below:")
    label2.place(x=150, y=175)
    label3 = tk.Label(window, text=list1)
    label3.place(x=150, y=200)

window = tk.Tk()

window.title("CSV Reader")
window.geometry("300x600")

user_file = tk.StringVar(window)

label1 = tk.Label(window, text="Enter full file path: ")
label1.place(x=25, y=100)
entry1 = tk.Entry(window, textvariable=user_file)
entry1.place(x=150, y=101)
button1 = tk.Button(window, text="Read File", command=file_entry)
button1.place(x=125, y=125)



window.mainloop()