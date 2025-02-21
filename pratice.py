import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)

root = tk.Tk()
root.title("File Upload Example")

label_file_explorer = tk.Label(root, text="Select a file", width=100, height=4, fg="blue")
label_file_explorer.grid(column=1, row=1)

button_explore = tk.Button(root, text="Browse Files", command=browse_file)
button_explore.grid(column=1, row=2)

root.mainloop()
