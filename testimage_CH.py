import tkinter as tk
from PIL import Image, ImageTk
import csv

# Create the main window
root = tk.Tk()
root.title("Display Images from CSV")

# Create a list to store the loaded images
image_list = []
current_image_index = 0
label = tk.Label(root)
with open('data\PuppyProfiles.csv', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        image_path = row['Profile Image']
        image = Image.open(image_path)
        resized =  image.resize((250, 255)) #you should resize based on the aspect ratio / 2
        myimage = ImageTk.PhotoImage(resized)
        image_list.append(myimage)
        
        
        print("current_image_index before IF statement:" + str(current_image_index))   


    for x in image_list:
        print("Length of array:" + str(len(image_list)))
        img_label = label.config(image=image_list[current_image_index])
        print(image_path)
        current_image_index +=1
        label = tk.Label(root)
        picButton = tk.Button(image=myimage)
        label.pack()
        picButton.pack()      


# Run the GUI
root.mainloop()


  