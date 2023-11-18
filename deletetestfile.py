import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

def delete_row():
    selected_index = row_combobox.current()
    if selected_index >= 0:
        df = pd.read_csv('data\PuppyProfiles.csv')  # Replace with your CSV file path

        df.drop(selected_index, inplace=True)
        df.reset_index(drop=True, inplace=True)

        df.to_csv('data\PuppyProfiles.csv', index=False)

        update_combobox()
        label.config(text=f"Row {selected_index + 1} deleted.")
    else:
        label.config(text="Please select a row.")

def update_combobox():
    df = pd.read_csv('data\PuppyProfiles.csv')  # Replace with your CSV file path
    row_combobox['values'] = df.index.tolist()

# Create the main window
root = tk.Tk()
root.title("Delete Row from CSV")

# Create a Combobox to select a row to delete
row_combobox = ttk.Combobox(root, state='readonly')
row_combobox.pack()

# Button to delete the selected row
delete_button = tk.Button(root, text="Delete Row", command=delete_row)
delete_button.pack()

# Label for status messages
label = tk.Label(root, text="")
label.pack()

# Update Combobox initially
update_combobox()

# Run the GUI
root.mainloop()