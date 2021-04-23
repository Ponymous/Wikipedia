import tkinter as tk
import os
import wikipedia
import tkinterhtml
from tkinter import ttk
from tkinter import filedialog, Text

root=tk.Tk()
root.wm_title('Wikipedia')
root.wm_iconbitmap('wiki_logo.ico')

root.grid_columnconfigure(0,weight=3)
root.grid_columnconfigure(1,weight=3)
root.grid_columnconfigure(2,weight=3)
root.grid_columnconfigure(3,weight=3)
root.grid_rowconfigure(0,weight=3)
root.grid_rowconfigure(1,weight=3)
root.grid_rowconfigure(2,weight=3)

def search():
    query=entry.get()
    page=wikipedia.page(f'{query}').content
    title=wikipedia.page(f'{query}').title

    title=tk.Label(root, text=title, font=("Times New Roman", 20, "bold"))
    title.grid(row=1, column=0, columnspan=2)

    text=tk.Text(root, font=("Times New Roman", 10))
    text.insert(tk.END, page)
    text.config(state='disabled')
    text.grid(row=2, column=0, columnspan=3, sticky='nesw')

label1=tk.Label(root, text="Search Wikipedia :", font=("Times New Roman", 10))
label1.grid(row=0, column=0)

entry=tk.Entry(root, width=30)
entry.grid(row=0, column=1)

button=tk.Button(root, text="Search", command=search)   
button.grid(row=0, column=2)

root.mainloop()