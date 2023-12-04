#!pip3 install pillow
#pip install pyimage
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from calendar import timegm
#from time import strftime
from datetime import date
from rapidfuzz import fuzz, process
from PIL import ImageTk, Image
import csv
import os
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
puppy_profile_file = 'data\PuppyProfiles.csv'
DOB = ''

class puppy_project(tk.Tk):
    def __init__(self):
        super().__init__()

        self.homepage()

    def homepage(self):
        self.title("Home Page")
        #self.delete_pet_row_from_file()
        # Create a Start Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Add New Pet", command=self.new_pet_page)
        self.search_button.grid(row=4, column=1, rowspan=20, padx=10, pady=10, sticky="ew")
        #delete pet
        self.search_button = tk.Button(self, text="Delete pet", command=self.delete_pet_page)
        self.search_button.grid(row=4, column=2, rowspan=20, padx=10, pady=10, sticky="ew")

        self.read_pet_profile_file()
        # Create a list to store the loaded images
        self.image_list = []
        #self.result =[]

        for x in range(0, len(self.df["Profile Image"])):
                
            
            pupImage = (self.df["Profile Image"].loc[int(x)])
            self.puppyProfileName = (self.df["Pets Name"].loc[int(x)])

            img = Image.open(pupImage)
            resized =  img.resize((250, 250)) #you should resize based on the aspect ratio / 2
            self.image_list.append(ImageTk.PhotoImage(resized))
        rowcounter = 0
        

        for x in range(0, len(self.image_list)):
            if((x % 3)==0):
                columncounter = 0
                rowcounter +=1

            self.img_label = Label(self, image=self.image_list[x])
            self.picButton = Button(self, image=self.image_list[x], command=lambda t=x: self.whichfile(t))
            self.picButton.grid(row=rowcounter, column=columncounter, padx=10, pady=10, sticky="ew")
            columncounter = columncounter+1
    
    #Adds a new pet to file.
    def whichfile(self, button_id):

        self.clickedyou = button_id
        #print(self.clickedyou)
        self.weight_entries_page()

    def write_new_csv_file(self, pet_name): #create file
        # Get user input for the file name and data
        folder_path = 'data'
        
        self.csv_file_name = pet_name+'.csv'

        # Combine the folder path and file name to create the full file path
        self.file_path = os.path.join(folder_path, self.csv_file_name)


        # Data to be written to the CSV file
        data = [
            ['WeightID', 'DateofEntry', 'Weight', 'Image', 'Comment']
        ]
        #Create csv file
        with open(self.file_path, 'w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file)
            csv_writer.writerows(data)
        #return file_path
        
    def add_new_pet(self, file=puppy_profile_file):
        
        PetID = self.df["PetID"].max() + 1
        pet_name = self.pet_name_entry.get()
        DOB = self.DOB_entry.get()
        breed = self.pet_breed_entry.get()
        image = self.filepath
        self.write_new_csv_file(pet_name)
        csvFile = self.file_path

        # Define the user data as a list
        user_data = [PetID, pet_name, DOB, breed, image, csvFile]

        try:
            # Open the CSV file in append mode
            with open(file, mode='a', newline='') as csvfile:
                # Create a CSV writer
                writer = csv.writer(csvfile)
                
                # Write the user data to the CSV file
                writer.writerow(user_data)
                
            print("User data added successfully.")
            self.submitted_message = tk.Label(self.pet_page, text="Pet was successfully added!" , font=('Ariel', 20))
            self.submitted_message.grid(row=5, column=1, padx=10, pady=10, sticky="e")
            self.submitted_message.grid

        except Exception as e:
            print(f"An error occurred: {e}")

    def upload_file(self):
        # Open a file dialog and let the user select an image file
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg')])
        #file_path = filedialog.askopenfilename()

        # Specify the folder to copy the file to
        destination_folder = "images"
        
        if file_path:
            
            # Use shutil to copy the file
            shutil.copy(file_path, destination_folder)

            self.filepath = destination_folder + '\\' + os.path.split(file_path)[1]
            #os.remove(self.filepath)

    def new_pet_page(self):

        self.pet_page=Toplevel()
        self.pet_page.title("Adding a New Pet")
        #self.pet_page.geometry("500x500")
 
        self.pet_page_label = tk.Label(self.pet_page, text="Enter New Pet Details:", font=('Ariel', 10))
        self.pet_page_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.pet_page_label.grid
       
        # Create a Label and place it on the left (column 0)
        #Label for Name:
        self.pet_name_label = tk.Label(self.pet_page, text="Pet's Name:") 
        self.pet_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.pet_name_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.pet_name_entry = tk.Entry(self.pet_page, width=30)
        self.pet_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew") 
       
        #Label for DOB:
        self.DOB_label = tk.Label(self.pet_page, text="Date of Birth (Example: 02/28/2023):")
        self.DOB_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.DOB_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.DOB_entry = tk.Entry(self.pet_page, width=30)
        self.DOB_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        #Label for Breed:
        self.pet_breed_label = tk.Label(self.pet_page, text="Pet's Breed:")
        self.pet_breed_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.pet_breed_label.grid

        #Entry widget for Breed:
        self.pet_breed_entry = tk.Entry(self.pet_page, width=30)
        self.pet_breed_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        #Label for Image:
        self.pet_image_label = tk.Label(self.pet_page, text="Select Profile Image:")
        self.pet_image_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.pet_image_label.grid

        # Create button to upload image.
        self.pet_image_btnOpen= tk.Button(self.pet_page, text="Upload Puppy Image", command=self.upload_file)
        self.pet_image_btnOpen.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        self.submit = tk.Label(self.pet_page, text="You must click 'Submit'" , font=('Ariel', 20))
        self.submit.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        self.submit.grid

        # Create a Submit Button and place it on the right (column 2)
        self.submit_btnOpen= tk.Button(self.pet_page, text="Submit", command=self.add_new_pet)
        self.submit_btnOpen.grid(row=5, column=3, padx=10, pady=10, sticky="ew")    

        #Buttons to Exit
        self.pet_page_buttonClose= tk.Button(self.pet_page, text="Exit", command=self.pet_page.destroy)
        self.pet_page_buttonClose.grid(row=6, column=3, padx=10, pady=10, sticky="ew") 

    def delete_pet_page(self):
        
        self.delete_pet=Toplevel()
        self.delete_pet.title("Delete a Pet")
        #self.delete_pet.geometry("500x500")
 
        self.delete_pet_label = tk.Label(self.delete_pet, text="Delete a Pet:", font=('Ariel', 10))
        self.delete_pet_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.delete_pet_label.grid
       
        # Create a Label and place it on the left (column 0)
        #Label for Name:
        self.delete_pet_label = tk.Label(self.delete_pet, text="Pet's Name:") 
        self.delete_pet_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.delete_pet_label.grid

        # Extract the column values from the DataFrame
        options = self.df['Pets Name'].tolist()        

        self.row_combobox = ttk.Combobox(self.delete_pet, values=options, state='readonly')
        self.row_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Create a button to update the label
        self.update_button = tk.Button(self.delete_pet, text="DELETE PET", command=self.delete_pet_row_from_file)
        self.update_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew") 
        self.update_button.grid

        #Buttons to Cancel
        self.delete_pet_buttonClose= tk.Button(self.delete_pet, text="Cancel", command=self.delete_pet.destroy)
        self.delete_pet_buttonClose.grid(row=6, column=3, padx=10, pady=10, sticky="ew") 
        self.delete_pet_buttonClose.grid

    # gets dog's profile based on PetID. (Gets dog's profile)
    def get_uniquedogprofile(self):
        '''returns dog's profiles based on petID.'''
        self.getAgeforProfileInfo()
        puppyName = (self.df["Pets Name"].loc[int(self.clickedyou)])
        puppyDOB = (self.df["Date of Birth"].loc[int(self.clickedyou)])
        Breed = (self.df["Breed"].loc[int(self.clickedyou)])

        self.entries_page.label = tk.Label(self.second_frame, text='Profile:', font=('Ariel', 15))
        self.entries_page.label.grid(row=1, column=4, padx=5, pady=5, sticky="ew")
        self.entries_page.label.grid

        self.entries_page.label = tk.Label(self.second_frame, text='Name: ' + puppyName)
        self.entries_page.label.grid(row=2, column=4, padx=5, pady=5, sticky="ew")
        self.entries_page.label.grid

        self.entries_page.label = tk.Label(self.second_frame, text='Date of Birth: ' + puppyDOB)
        self.entries_page.label.grid(row=3, column=4, padx=5, pady=5, sticky="ew")
        self.entries_page.label.grid

        self.entries_page.label = tk.Label(self.second_frame, text='Current Age: ' + str(self.ageInMonths) + " months")
        self.entries_page.label.grid(row=4, column=4, padx=5, pady=5, sticky="ew")
        self.entries_page.label.grid

        self.entries_page.label = tk.Label(self.second_frame, text='Breed: ' + Breed)
        self.entries_page.label.grid(row=5, column=4, padx=5, pady=5, sticky="ew")
        self.entries_page.label.grid    
        #self.entries_page .label = tk.Label(self.entries_page, text='Name: ' + puppyName + '\n Date of Birth: ' + puppyDOB + '\n Breed: ' + Breed)

    #Plots csv file into image label
    def plotcsv(self):
        
        self.read_pet_file_from_csv()
        '''Plots pet csv file based on PetID selected by user. '''
        # Read the CSV file into a DataFrame
        
        # Extract X and Y data
        x = self.readFile['DateofEntry']
        y = self.readFile['Weight']

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('Date of Entry')
        ax.set_ylabel('Weight')

        # Save the figure to a BytesIO object
        buf = io.BytesIO()
        FigureCanvas(fig).print_png(buf)

        #Load this into a PIL image
        buf.seek(0)
        img = Image.open(buf)

        # Convert the PIL image into a PhotoImage
        self.photo = ImageTk.PhotoImage(img)

    def weight_entries_page(self):
        
        self.plotcsv()
        self.entries_page=Toplevel()
        self.read_path_location_from_csv()
        pupName = (self.df["Pets Name"].loc[int(self.clickedyou)])

        self.entries_page.geometry('800x800')
        self.entries_page.minsize(800,800)
        #create a main frame
        main_frame = Frame(self.entries_page)
        main_frame.pack(fill=BOTH, expand=1)

        #create a canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # add a scrollbar to the canvas
        my_scrollbar_x = tk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        my_scrollbar_x.pack(side=BOTTOM, fill=X)
        my_canvas.configure(xscrollcommand=my_scrollbar_x.set) #configure the canvas 

        # add a vertical scrollbar to the canvas
        my_scrollbar_y = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar_y.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar_y.set) #configure the canvas

        main_frame.bind("<Configure>", lambda event, canvas=my_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # create another fram inside the canvas 
        self.second_frame = Frame(my_canvas)

        #add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=self.second_frame, anchor='nw')

        self.entries_page.title("Entries for pet: " + pupName)
        self.get_uniquedogprofile() #display's dog's profile
        
        # plot image
        self.entries_page.label = tk.Label(self.second_frame, image=self.photo)
        #self.entries_page.label.image = self.photo  # keep a reference to the image
        self.entries_page.label.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        #self.entries_page.label.grid

        self.entries_page.label = tk.Label(self.second_frame, text=pupName, font=('Ariel', 30))
        self.entries_page.label.grid(row=0, column=2, sticky="ew")
        #self.entries_page.label.grid

        self.get_puppy_profile_image() # get's profile's image

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.entries_page.btnOpen=Button(self.second_frame, text="Add new weight record:", command=self.add_weight_page)
        self.entries_page.btnOpen.grid(row=3, column=0, padx=10, pady=10, sticky="ew")  
        #self.entries_page.btnOpen.grid

        #Tiles for Previous records:
        self.entries_page.label = tk.Label(self.second_frame, text="Previous weight records: ", font=('Ariel', 20))
        self.entries_page.label.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        #self.entries_page.label.grid

        self.print_indvidual_entry_record() 

    def get_puppy_profile_image(self):

        self.new_image_list = []

        puppyImage = (self.df["Profile Image"].loc[int(self.clickedyou)])

        img = Image.open(puppyImage)
        resized =  img.resize((325, 300)) #you should resize based on the aspect ratio / 2
        self.new_image_list.append(ImageTk.PhotoImage(resized))

        self.entries_page.label = tk.Label(self.second_frame, image=self.new_image_list)
        self.entries_page.label.grid(row=0, column=4, sticky="ew")
        #self.entries_page.label.grid

    #Read PetProfile csv file
    def read_pet_profile_file(self, petProfileCSV=puppy_profile_file):

        self.df = pd.read_csv(petProfileCSV)

    #Adds new row to file for new pet weight record
    def new_weight_record(self):
        
        weightID = self.readFile['WeightID'].max() + 1
        pet_csv_file = self.pupCSVPath
        input_date = self.input_date_entry.get()
        weight = self.weight_entry.get()
        image = self.filepath
        comment = self.comment_entry.get()
        # Define the user data as a list
        weight_user_data = [weightID, input_date, weight, image, comment]

        try:
            # Open the CSV file in append mode
            with open(pet_csv_file, mode='a', newline='') as new_pet_csv_file:
                # Create a CSV writer
                writer = csv.writer(new_pet_csv_file)
                # Write the user data to the CSV file
                writer.writerow(weight_user_data)
                
            print("User data added successfully.")
            # Show to user the entry was added.
            self.submit_weight_message=Label(self.new_weight, text="New weight record submitted.", font=('Ariel', 15))
            self.submit_weight_message.grid(row=9, column=1, padx=10, pady=20, sticky="ew")    
            self.submit_weight_message.grid
            
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def add_weight_page(self):

        self.new_weight=Toplevel()
        #self.read_path_location_from_csv()
        pupName = (self.df["Pets Name"].loc[int(self.clickedyou)])
        self.new_weight.title("New Weight for " + pupName)
        #self.new_weight.geometry("500x500")

        self.new_weight_label = tk.Label(self.new_weight, text="Enter New Pet Details for " + pupName, font=('Ariel', 16))
        self.new_weight_label.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        self.new_weight_label.grid
        # Create a Label and place it on the left (column 0)
        #Label for Name:
        self.input_date_label = tk.Label(self.new_weight, text="Date of Entry (Example: 02/28/2023):") 
        self.input_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.input_date_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.input_date_entry = tk.Entry(self.new_weight, width=30) #entry = textbox single line for text
        self.input_date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        #Label for DOB:
        self.weight_label = tk.Label(self.new_weight, text="Weight:")
        self.weight_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.weight_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.weight_entry = tk.Entry(self.new_weight, width=30) #entry = textbox single line for text
        self.weight_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        #Label for Image:
        self.image_label = tk.Label(self.new_weight, text="Upload Image:")
        self.image_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.image_label.grid

        #Create button to upload image.
        self.image_btnOpen=Button(self.new_weight, text="Upload Image", command=self.upload_file)
        self.image_btnOpen.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        #Label for Comments:
        self.comment_label = tk.Label(self.new_weight, text="Comments:")
        self.comment_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.comment_label.grid

        #Entry widget for Breed:
        self.comment_entry = tk.Entry(self.new_weight, width=30)
        self.comment_entry.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        # Create a Submit Button and place it on the right (column 2)
        self.submit_btnOpen=Button(self.new_weight, text="Submit", command=self.new_weight_record)
        self.submit_btnOpen.grid(row=8, column=1, padx=10, pady=20, sticky="ew")    
        self.submit_btnOpen.grid

        #Buttons to Exit
        self.new_weight.buttonClose=Button(self.new_weight, text="Exit", command=self.destroy)
        self.new_weight.buttonClose.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    def read_path_location_from_csv(self):

        self.pupCSVPath = (self.df["csvFile"].loc[int(self.clickedyou)])

    #Read CSV file from puppy profile
    def read_pet_file_from_csv(self):  

        self.readFile = pd.read_csv(self.df["csvFile"].loc[int(self.clickedyou)]) #reads the file for each individual puppy. (Their weight record)

    #Prints out individual pet's row records, e.g. an entry for a day
    def print_indvidual_entry_record(self):

        self.weightImage = []
        rowcounter = 6
        columncounter = 0

        for x in range(0, len(self.readFile)):  
            #print("BEGINNING: " + str(rowcounter))
            if((x % 5)==0) and (x != 0):
                columncounter = 0
                rowcounter +=5
            weightpuppyImage = (self.readFile["Image"].loc[x])           
            dateofEntryRecord = (self.readFile["DateofEntry"].loc[x])
            weightRecord = (self.readFile["Weight"].loc[x])
            comment = (self.readFile["Comment"].loc[x])

            myimg = Image.open(weightpuppyImage)
            imgresized =  myimg.resize((150, 200)) #you should resize based on the aspect ratio / 2
            self.weightImage.append(ImageTk.PhotoImage(imgresized))
            self.entries_page.label = tk.Label(self.second_frame, image=self.weightImage[x])
            self.entries_page.label.grid(row=rowcounter+0, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            self.entries_page.label = tk.Label(self.second_frame, text='Date of Entry: ' + dateofEntryRecord)
            self.entries_page.label.grid(row=rowcounter+1, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            self.entries_page.label = tk.Label(self.second_frame, text='Weight Record: ' + str(weightRecord))
            self.entries_page.label.grid(row=rowcounter+2, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid    

            self.entries_page.label = tk.Label(self.second_frame, text='Comment: ' + comment)
            self.entries_page.label.grid(row=rowcounter+3, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            self.entries_page.btnOpen=Button(self.second_frame, text="Delete this record:", command=lambda m=x: self.delete_weight_row_from_file(m))
            self.entries_page.btnOpen.grid(row=rowcounter+4, column=columncounter, columnspan=1, padx=10, pady=10, sticky="ew")  
            columncounter = columncounter+1

    # Delete row from weight file
    def delete_weight_row_from_file(self, delete_weight):

        myselected_row = self.readFile.iloc[int(delete_weight)] #this is the row of weight record
        #myselected_row['WeightID'] #returns the ID of the selected row

        # Filter the DataFrame to remove the row(s) matching the criteria
        df = self.readFile[self.readFile['WeightID'] != myselected_row['WeightID']]  #DateofEntry is the column to identify the row
        # Save the updated DataFrame back to the CSV file
        df.to_csv(self.pupCSVPath, index=False)

        print(f"Row for {delete_weight} has been deleted from the CSV file.")  

    #Calculates age
    def getAgeforProfileInfo(self): #DOB = '01/05/2023', , date_of_entry = '05/02/2023'
        """Calculate the age based on all of the Date fields from the PetRecord.csv file and compares to the DOB field from the pets.csv file."""
        self.read_pet_file_from_csv()
        self.read_pet_profile_file()

        #read dateofEntry for weight
        date_of_entry = date.today()

        DOB = self.df["Date of Birth"].loc[self.clickedyou]
        DOButc_time = time.strptime(DOB + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
        DOBepoch_time = timegm(DOButc_time)
        
        #DOEepoch_time = time.strptime(date_of_entry + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
        DOEepoch_time = timegm(date_of_entry.timetuple())

        #Calculate the age
        age = DOEepoch_time - DOBepoch_time #Subtract the DateOfEntry = DateOfBirth
        self.ageInMonths = int(age/(60 * 60 * 24 * 30))

        #print("Days: " + str(age/(3600 * 24))) # ((60 seconds * 60 minutes) = 3600 * 24 hours)
        #print("Months: " + str(age/(60 * 60 * 24 * 30))) # (60 seconds * 60 minutes * 24 hours * 30 days)
        #print("Years: " + str(age/(3600 * 24 * 365))) # ((60 seconds * 60 minutes) = 3600 seconds * 24 hours * 365 days)

 #Calculates age
    def getAgeforPlot(self): #DOB = '01/05/2023', , date_of_entry = '05/02/2023'
        """Calculate the age based on all of the Date fields from the PetRecord.csv file and compares to the DOB field from the pets.csv file."""

        self.agelist = []

        self.read_pet_file_from_csv() #read the weight results for dutton
        #print('..............................Print readFile................................')
        #print(self.readFile) #reads the file for each individual puppy. (Their weight record)
        self.read_pet_profile_file() #read the profileInfo for DOB

        for x in range(len(self.readFile)):

            date_of_entry = (self.readFile["DateofEntry"].loc[x])

            #print('..............................Print date_of_entry................................')
            #print('dateofentry', {date_of_entry})  

            DOB = self.df["Date of Birth"].loc[self.clickedyou]
            #print('DOB', {DOB})

            DOButc_time = time.strptime(DOB + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
            DOBepoch_time = timegm(DOButc_time)

            DOEutc_time = time.strptime(date_of_entry + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
            DOEepoch_time = timegm(DOEutc_time)
            #Calculate the age
            age = DOEepoch_time - DOBepoch_time #Subtract the DateOfEntry = DateOfBirth
            ageInMonthsforplotting = int(age/(60 * 60 * 24 * 30))
            #print("Age ", ageInMonthsforplotting, "months")
            self.agelist.append(ageInMonthsforplotting)
            #print("Days: " + str(age/(3600 * 24))) # ((60 seconds * 60 minutes) = 3600 * 24 hours)
            #print("Months: " + str(age/(60 * 60 * 24 * 30))) # (60 seconds * 60 minutes * 24 hours * 30 days)
            #print("Years: " + str(age/(3600 * 24 * 365))) # ((60 seconds * 60 minutes) = 3600 seconds * 24 hours * 365 days)
            #print(self.agelist)
    #Returns individual pet's weight COLUMN ONLY records
    def print_weight_record_for_individual(self):
        
        self.read_pet_file_from_csv()
        r = input("What weight do you wan to return?")
        self.unique_weight = (self.readFile["Weight"].loc[int(r)])
        #print({unique_weight})

    # Delete file from profile file
    def delete_pet_row_from_file(self, file=puppy_profile_file):
        
        self.df = pd.read_csv(file)
        
        print(self.row_combobox.current())

        #Delete the CSV file before deleting the row.
        csvFileToDelete = self.df["csvFile"].loc[self.row_combobox.current()]
        self.delete_csv_file(csvFileToDelete)

        # Filter the DataFrame to remove the row(s) matching the criteria
        self.df = self.df[self.df['PetID'] != self.row_combobox.current()]
        #Save the updated DataFrame back to the CSV file
        self.df.to_csv(file, index=False)
        print('file successfully deleted')

        #Text to show it was deleted
        self.delete_pet_message= tk.Label(self.delete_pet, text="Pet was successfully deleted!", font=('Ariel', 15))
        self.delete_pet_message.grid(row=6, column=1, padx=10, pady=10, sticky="ew") 
        self.delete_pet_message.grid
 
    # Deletes csv file when pet is deleted
    def delete_csv_file(self, csv_file):

        # Check if the file exists before attempting to delete it
        if os.path.exists((csv_file)):
            os.remove((csv_file))
            print(f"CSV file '{csv_file}' has been deleted.")
        else:
            print(f"CSV file '{csv_file}' does not exist.")

app=puppy_project()#
app.mainloop()