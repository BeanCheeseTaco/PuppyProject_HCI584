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
    
    ################################### Home Page ################################
    ''' This is the starting point. Shows user images of existing pets and allows adding or deleting of pet. 
        Here we will run through a for loop that reads the images from the puppy profile csv file. It then only shows
        up to 3 images per row. 
    '''
    def homepage(self):
        self.title("Home Page")

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



    ################################### Read csv files ################################
    ''' These functions are used to read csv files. It begins with the puppy profile csv then reads which pet was 
        selected on the home page.'''
        
    #Read PetProfile csv file
    def read_pet_profile_file(self, petProfileCSV=puppy_profile_file):
        '''Used to read the petprofile csv'''
        self.df = pd.read_csv(petProfileCSV)

    #self.pupCSVPath is used to delete in the delete_weight_row_from_file() function and add weight record in the new_weight_record() functions only.
    def read_path_location_from_csv(self):
        '''Reads csv file for reading and writing to the csv file of the pet selected'''
        self.pupCSVPath = (self.df["csvFile"].loc[int(self.clickedyou)])

    #Read CSV file from puppy profile
    def read_pet_file_from_csv(self):  
        '''Used to read the csv file of the pet selected in the puppyprofile csv. Reads the file for each individual puppy, i.e. weight records'''
        self.readFile = pd.read_csv(self.df["csvFile"].loc[int(self.clickedyou)]) 

    #which option was clicked by user on the homepage.
    def whichfile(self, button_id):
        '''Used to choose which record was selected on the home page, then opens the pet's page that shows their information'''
        self.clickedyou = button_id
        self.weight_entries_page()



################################### Add New Pet ################################
    ''' This section covers the functions used to add a new pet including the new pet page. '''
    #Page to add new pet
    def new_pet_page(self):
        '''This function adds the fields for users to add a new pet.'''
        self.pet_page=Toplevel()
        self.pet_page.title("Adding a New Pet")
  
        self.pet_page_label = tk.Label(self.pet_page, text="Enter New Pet Details:", font=('Ariel', 10))
        self.pet_page_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.pet_page_label.grid
       
        #Label for Name:
        self.pet_name_label = tk.Label(self.pet_page, text="Pet's Name:") 
        self.pet_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.pet_name_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters) for the Pet's Name
        self.pet_name_entry = tk.Entry(self.pet_page, width=30)
        self.pet_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew") 
       
        #Label for DOB with instructions on the DOB format
        self.DOB_label = tk.Label(self.pet_page, text="Date of Birth (Example: 02/28/2023):")
        self.DOB_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.DOB_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters) for the Date of Birth
        self.DOB_entry = tk.Entry(self.pet_page, width=30)
        self.DOB_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        #Label for Breed:
        self.pet_breed_label = tk.Label(self.pet_page, text="Pet's Breed:")
        self.pet_breed_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.pet_breed_label.grid

        #Entry widget with a specific width (e.g., 30 characters) for the Breed
        self.pet_breed_entry = tk.Entry(self.pet_page, width=30)
        self.pet_breed_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        #Label for Image:
        self.pet_image_label = tk.Label(self.pet_page, text="Select Profile Image:")
        self.pet_image_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.pet_image_label.grid

        # Create button to upload a profile image which is added to the puppyprofile csv
        self.pet_image_btnOpen= tk.Button(self.pet_page, text="Upload Puppy Image", command=self.upload_image)
        self.pet_image_btnOpen.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # Label with instructions letting the user know they need to click on Submit.
        self.submit = tk.Label(self.pet_page, text="You must click 'Submit'" , font=('Ariel', 20))
        self.submit.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        self.submit.grid

        # Create a Submit Button
        self.submit_btnOpen= tk.Button(self.pet_page, text="Submit", command=self.add_new_pet)
        self.submit_btnOpen.grid(row=5, column=3, padx=10, pady=10, sticky="ew")    

        #Buttons to Exit
        self.pet_page_buttonClose= tk.Button(self.pet_page, text="Exit", command=self.pet_page.destroy)
        self.pet_page_buttonClose.grid(row=6, column=3, padx=10, pady=10, sticky="ew") 
    
    # #create new csv file when a pet is created
    def write_new_csv_file(self, pet_name): 
        '''Get user input for the file name and data'''
        folder_path = 'data' #declare what folder path the csv will be added to
        
        self.csv_file_name = pet_name+'.csv' #declares variable to get the name format of the pet's name + .csv

        self.file_path = os.path.join(folder_path, self.csv_file_name) # Combine the folder path and file name to create the full file path

        # Data to be written to the CSV file. These will be the header row.
        data = [
            ['WeightID', 'DateofEntry', 'Weight', 'Image', 'Comment']
        ]
        #Create csv file
        with open(self.file_path, 'w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file)
            csv_writer.writerows(data)
        
    # add_new_pet to puppyprofile csv file
    def add_new_pet(self, file=puppy_profile_file):
        ''' Create a list called user_data and add the user input and add this to the puppyprofile csv'''

        PetID = self.df["PetID"].max() + 1 #increment petID by the max petID.
        pet_name = self.pet_name_entry.get() #get user input for petname.
        DOB = self.DOB_entry.get()  #get user input for DOB.
        breed = self.pet_breed_entry.get() #get user input for breed.
        image = self.filepath #get user input for image.
        self.write_new_csv_file(pet_name) #call for write_new_csv_file function
        csvFile = self.file_path #get csv file from csv file we created using the pet name. 

        user_data = [PetID, pet_name, DOB, breed, image, csvFile] # Define the user data as a list

        try:
            # Open the CSV file in append mode
            with open(file, mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile)  # Create a CSV writer

                writer.writerow(user_data) # Write the user data to the CSV file
                
            print("User data added successfully.") #print on console that it was added. 

            #show to the user the pet was added. 
            self.submitted_message = tk.Label(self.pet_page, text="Pet was successfully added!" , font=('Ariel', 20)) 
            self.submitted_message.grid(row=5, column=1, padx=10, pady=10, sticky="e")
            self.submitted_message.grid

        except Exception as e:
            print(f"An error occurred: {e}")
    
    #uploads image to image folder.
    def upload_image(self):
        ''' uploads image from user input'''
        
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg')]) # Open a file dialog and let the user select an image file

        destination_folder = "images"  # Specify the folder to copy the image to. 
        
        if file_path:
            
            shutil.copy(file_path, destination_folder)  # Use shutil to copy the file

            self.filepath = destination_folder + '\\' + os.path.split(file_path)[1] 




################################### Individual Pet Page ################################
    # This is the 'Entries for pet page' which shows the profile, scrollbar, plot
    def weight_entries_page(self):
        '''Display the page that will show the pet data. '''
        self.entries_page=Toplevel()
        self.plotcsv() 
        self.read_path_location_from_csv()
        pupName = (self.df["Pets Name"].loc[int(self.clickedyou)]) #get the pet's name of the entry that was selected in the petprofilepage (homepage)

        #set page size
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

        # create another frame inside the canvas 
        self.second_frame = Frame(my_canvas)

        #add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=self.second_frame, anchor='nw')

        self.entries_page.title("Entries for pet: " + pupName) #set the title
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

        # Create an button to take us to the add_weight_page 
        self.entries_page.btnOpen=Button(self.second_frame, text="Add new weight record", command=self.add_weight_page)
        self.entries_page.btnOpen.grid(row=3, column=0, padx=10, pady=10, sticky="ew")  

        #Title for previous records:
        self.entries_page.label = tk.Label(self.second_frame, text="Previous weight records: ", font=('Ariel', 20))
        self.entries_page.label.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.print_indvidual_weight_record() #this will show the tiles of the previous weight records. 

    # gets dog's profile based on PetID. (Gets dog's profile)
    def get_uniquedogprofile(self):
        '''returns dog's profiles based on petID so we can use on the weight_entries_page'''
        self.getAgeforProfileInfo() #function that calcuates the age
        puppyName = (self.df["Pets Name"].loc[int(self.clickedyou)]) #get puppyname based on the homepage selection
        puppyDOB = (self.df["Date of Birth"].loc[int(self.clickedyou)]) #get DOB based on the homepage selection
        Breed = (self.df["Breed"].loc[int(self.clickedyou)]) #get Breed based on the homepage selection

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

    #Plots csv file into image label
    def plotcsv(self):
        '''Plots pet csv file based on PetID selected by user. '''
        self.read_pet_file_from_csv() # Read the CSV file into a DataFrame
        
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

    # get's profile image and prints image in a label.
    def get_puppy_profile_image(self):
        ''' gets the image stored in the puppyprofile csv file to show on the weight_entries_page profile section'''
        self.new_image_list = [] #set sempty list.

        puppyImage = (self.df["Profile Image"].loc[int(self.clickedyou)]) #get image for the pet selected on homepage.

        img = Image.open(puppyImage) #open image
        resized =  img.resize((325, 300)) #resizing image
        self.new_image_list.append(ImageTk.PhotoImage(resized)) #appending resized image to list. 

        self.entries_page.label = tk.Label(self.second_frame, image=self.new_image_list) #display image via a label
        self.entries_page.label.grid(row=0, column=4, sticky="ew")

    #Calculates age for the profile section of the pet. 
    def getAgeforProfileInfo(self):
        '''Calculate the age based on today and compares to the DOB field from the petprofile csv file.'''
        #self.read_pet_file_from_csv() #Reads weight record from pet's invividual csv
        self.read_pet_profile_file() #Reads PetProfile csv to get the DOB field.

        date_of_entry = date.today() #Get today's date for weight

        DOB = self.df["Date of Birth"].loc[self.clickedyou] #get DOB for pet selected on home page
        DOButc_time = time.strptime(DOB + ' 00:00:00', "%m/%d/%Y %H:%M:%S") 
        DOBepoch_time = timegm(DOButc_time)
        
        #DOEepoch_time = time.strptime(date_of_entry + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
        DOEepoch_time = timegm(date_of_entry.timetuple())

        #Calculate the age
        age = DOEepoch_time - DOBepoch_time #Subtract the DateOfEntry from DateOfBirth
        self.ageInMonths = int(age/(60 * 60 * 24 * 30)) #get age in months
 
    #Prints out individual pet's row records, e.g. an entry for a day
    def print_indvidual_weight_record(self):
        '''gets each weight record from the pet selected and saves to list weightImage. Then prints them, 5 per row'''
        self.weightImage = []
        rowcounter = 6 #starting at 6 as this is row we're starting to print at.
        columncounter = 0 

        for x in range(0, len(self.readFile)):  #read through file
            if((x % 5)==0) and (x != 0):
                columncounter = 0
                rowcounter +=5
            weightpuppyImage = (self.readFile["Image"].loc[x])  #get image from the row         
            dateofEntryRecord = (self.readFile["DateofEntry"].loc[x]) #get DateofEntry from the row   
            weightRecord = (self.readFile["Weight"].loc[x]) #get weight from the row   
            comment = (self.readFile["Comment"].loc[x]) #get comment from the row   

            myimg = Image.open(weightpuppyImage) #open the image
            imgresized =  myimg.resize((150, 200)) #resize image
            self.weightImage.append(ImageTk.PhotoImage(imgresized)) #append to list

            #label for each image.
            self.entries_page.label = tk.Label(self.second_frame, image=self.weightImage[x])
            self.entries_page.label.grid(row=rowcounter+0, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            #label for each dateofentry record.
            self.entries_page.label = tk.Label(self.second_frame, text='Date of Entry: ' + dateofEntryRecord)
            self.entries_page.label.grid(row=rowcounter+1, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            #label for each weight that was recorded.
            self.entries_page.label = tk.Label(self.second_frame, text='Weight Record: ' + str(weightRecord))
            self.entries_page.label.grid(row=rowcounter+2, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid    

            #label for each comment.
            self.entries_page.label = tk.Label(self.second_frame, text='Comment: ' + str(comment))
            self.entries_page.label.grid(row=rowcounter+3, column=columncounter, columnspan=1, padx=10, pady=10, sticky="e")
            self.entries_page.label.grid

            #Button to give the user the option to delete each row if they would like.
            self.entries_page.btnOpen=Button(self.second_frame, text="Delete this record", command=lambda m=x: self.delete_weight_row_from_file(m))
            self.entries_page.btnOpen.grid(row=rowcounter+4, column=columncounter, columnspan=1, padx=10, pady=10, sticky="ew")  
            columncounter = columncounter+1 #increment column to add the column for each record on a new column. 



################################### Add new weight record ################################
    #Page to allow user to add new weight record. 
    def add_weight_page(self):
        ''' This will show a page to the user to add a new weight record'''
        self.new_weight=Toplevel()

        pupName = (self.df["Pets Name"].loc[int(self.clickedyou)]) #get pet name for the pet selected on homepage
        self.new_weight.title("New Weight for " + pupName) #print the name in the title

        #Label showing the pet name.
        self.new_weight_label = tk.Label(self.new_weight, text="Enter New Pet Details for " + pupName, font=('Ariel', 16))
        self.new_weight_label.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        self.new_weight_label.grid

        #Label for Date of Entry:
        self.input_date_label = tk.Label(self.new_weight, text="Date of Entry (Example: 02/28/2023):") 
        self.input_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.input_date_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters) for the Date of Entry.
        self.input_date_entry = tk.Entry(self.new_weight, width=30) #entry = textbox single line for text
        self.input_date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        #Label for DOB:
        self.weight_label = tk.Label(self.new_weight, text="Weight:")
        self.weight_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.weight_label.grid

        # Create an Entry Widget with a specific width (e.g., 30 characters) for the weight.
        self.weight_entry = tk.Entry(self.new_weight, width=30) 
        self.weight_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        #Label for Image:
        self.image_label = tk.Label(self.new_weight, text="Upload Image:")
        self.image_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.image_label.grid

        #Create button to upload image.
        self.image_btnOpen=Button(self.new_weight, text="Upload Image", command=self.upload_image)
        self.image_btnOpen.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        #Label for Comments:
        self.comment_label = tk.Label(self.new_weight, text="Comments:")
        self.comment_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.comment_label.grid

        #Create an Entry Widget with a specific width (e.g., 30 characters) for the comment.
        self.comment_entry = tk.Entry(self.new_weight, width=30)
        self.comment_entry.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        # Create a Submit Button for the data entered.
        self.submit_btnOpen=Button(self.new_weight, text="Submit", command=self.new_weight_record)
        self.submit_btnOpen.grid(row=8, column=1, padx=10, pady=20, sticky="ew")    
        self.submit_btnOpen.grid

        #Buttons to Exit
        self.new_weight.buttonClose=Button(self.new_weight, text="Exit", command=self.destroy)
        self.new_weight.buttonClose.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    #Adds new row to file for new pet weight record
    def new_weight_record(self):
        ''' create a new list called weight_user_data to add the new weight records to for the pet selected in the home page.'''

        weightID = self.readFile['WeightID'].max() + 1 #get the max weightiD and increment by 1. 
        pet_csv_file = self.pupCSVPath #get the csvpath for where to store.
        input_date = self.input_date_entry.get() #get the date input by the user.
        weight = self.weight_entry.get() #get the weight input by the user.
        image = self.filepath #get the image input by the user.
        comment = self.comment_entry.get() #get the comment input by the user.
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



################################### Delete Pet ################################
    # Page to allow users to delete a pet. 
    def delete_pet_page(self):
        '''User selects a net from a drop down using combobox and can delete that user selected via the pet's name which uses the Pet ID.'''
        self.delete_pet=Toplevel()
        self.delete_pet.title("Delete a Pet") #set title

        #Lable to Delete a pet.
        self.delete_pet_label = tk.Label(self.delete_pet, text="Delete a Pet:", font=('Ariel', 10))
        self.delete_pet_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.delete_pet_label.grid
       
        #Label for Pet Name:
        self.delete_pet_label = tk.Label(self.delete_pet, text="Pet's Name:") 
        self.delete_pet_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.delete_pet_label.grid

        # Extract the column values from the DataFrame
        options = self.df['Pets Name'].tolist()        
        #Combox for drop down.
        self.row_combobox = ttk.Combobox(self.delete_pet, values=options, state='readonly')
        self.row_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Create a button to delete the pet
        self.update_button = tk.Button(self.delete_pet, text="DELETE PET", command=self.delete_pet_from_csv)
        self.update_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew") 
        self.update_button.grid

        #Buttons to Cancel if user no longer wants to delete the pet.
        self.delete_pet_buttonClose= tk.Button(self.delete_pet, text="Cancel", command=self.delete_pet.destroy)
        self.delete_pet_buttonClose.grid(row=6, column=3, padx=10, pady=10, sticky="ew") 
        self.delete_pet_buttonClose.grid

    #Delete file from profile file
    def delete_pet_from_csv(self, file=puppy_profile_file):
        ''' This will delete the pet and delete the csv file that's tied to the pet when the pet is deleted.'''
        self.df = pd.read_csv(file) #read petprofile csv
        
        print(self.row_combobox.current()) #get selected pet

        #Delete the CSV file before deleting the row.
        csvFileToDelete = self.df["csvFile"].loc[self.row_combobox.current()]
        self.delete_csv_file(csvFileToDelete) #delete the csv by calling the delete_csv_file method.

        # Filter the DataFrame to remove the row(s) matching the criteria
        self.df = self.df[self.df['PetID'] != self.row_combobox.current()] #use PetID to delete pet by as the PetID should be unique.

        #Save the updated DataFrame back to the CSV file
        self.df.to_csv(file, index=False)
        print('file successfully deleted')

        #Show the user the pet was deleted
        self.delete_pet_message= tk.Label(self.delete_pet, text="Pet was successfully deleted!", font=('Ariel', 15))
        self.delete_pet_message.grid(row=6, column=1, padx=10, pady=10, sticky="ew") 
        self.delete_pet_message.grid

    # Deletes csv file when pet is deleted
    def delete_csv_file(self, csv_file):
        '''deletes the csv file if the file exists'''
        # Check if the file exists before attempting to delete it
        if os.path.exists((csv_file)):
            os.remove((csv_file))
            print(f"CSV file '{csv_file}' has been deleted.")
        else:
            print(f"CSV file '{csv_file}' does not exist.")



################################### Delete Weight Record ################################
    # Delete row from weight file 
    def delete_weight_row_from_file(self, delete_weight):
        ''' delete a weight row from the puppy's unique file if requested'''
        myselected_row = self.readFile.iloc[int(delete_weight)] #read file, this is the row of weight record

        # Filter the DataFrame to remove the row(s) matching the criteria
        df = self.readFile[self.readFile['WeightID'] != myselected_row['WeightID']]  #WeightID is the column to identify the row
        # Save the updated DataFrame back to the CSV file
        df.to_csv(self.pupCSVPath, index=False)

        print(f"Row for {delete_weight} has been deleted from the CSV file.")  #print on console if the row was deleted.
        
        #Show user via a message the record was deleted.
        self.entries_page.label = tk.Label(self.second_frame, text='Weight record was deleted', font=('Ariel', 20))
        self.entries_page.label.grid(row=4, column=0, padx=10, pady=10, sticky="ew")


app=puppy_project()
app.mainloop()