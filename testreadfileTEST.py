import tkinter as tk
from tkinter import ttk
import pandas as pd

def update_label():
    # Read the CSV file into a DataFrame
    csv_file = 'data\Dutton.csv'  # Replace with your CSV file path
    df = pd.read_csv(csv_file)

    # Get the information to display
    selected_row = df.iloc[row_var.get()]

    # Update the label text
    label.config(text=f"Name: {selected_row['DateofEntry']}, Age: {selected_row['Weight']}, Location: {selected_row['Image']}")

# Create the main window
root = tk.Tk()
root.title("Tkinter Label from CSV")

# Create a label
label = tk.Label(root, text="")
label.pack()

# Create a Combobox to select a row from the CSV file
csv_file = 'data\Dutton.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)
row_var = tk.IntVar(value=0)
rows = list(range(len(df)))
row_combobox = ttk.Combobox(root, textvariable=row_var, values=rows, state='readonly')
row_combobox.pack()

# Create a button to update the label
update_button = tk.Button(root, text="Update Label", command=update_label)
update_button.pack()

# Run the GUI
root.mainloop()