import tkinter as tk
from tkinter import ttk
import pandas as pd

def show_selected():
    selected_value = combo_box.get()
    label.config(text=f"Selected value: {selected_value}")

# Read the CSV file into a DataFrame
csv_file = 'data\PuppyProfiles.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Extract the column values from the DataFrame
options = df['Pets Name'].tolist()

# Create the main window
root = tk.Tk()
root.title("Tkinter Combobox from CSV")

# Create a Combobox with values from the CSV file
combo_box = ttk.Combobox(root, values=options, state='readonly')
combo_box.pack()

# Button to show the selected value
show_button = tk.Button(root, text="Show Selected", command=show_selected)
show_button.pack()

# Label to display the selected value
label = tk.Label(root, text="")
label.pack()

# Run the GUI
root.mainloop()