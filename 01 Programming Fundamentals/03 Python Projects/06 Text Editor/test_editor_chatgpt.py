import tkinter as tk
from tkinter import filedialog

def open_file():
    """
    Opens a file dialog to select a file and displays its content in the text widget.
    """
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, "r") as file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())

def save_file():
    """
    Opens a file dialog to choose a location to save the text content in the text widget.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text.get("1.0", tk.END))

# Create the main application window
root = tk.Tk()
root.title("Text Editor")
root.geometry("500x500")

# Create a Text widget for displaying and editing text
text = tk.Text(root)
text.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Create "Open" button and associate it with the open_file function
open_button = tk.Button(root, text="Open", command=open_file)
open_button.grid(row=1, column=0, sticky="nsew")

# Create "Save" button and associate it with the save_file function
save_button = tk.Button(root, text="Save", command=save_file)
save_button.grid(row=2, column=0, sticky="nsew")

# Configure row and column weights to make the Text widget expand with the window
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()

