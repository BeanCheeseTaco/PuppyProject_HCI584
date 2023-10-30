# This is a .py export from your main.ipynb notebook!


#!pip3 install pillow
import pandas as pd
import time
from calendar import timegm
from time import strftime
import datetime
from rapidfuzz import fuzz, process
from PIL import Image
import csv
import os
DATA_FOLDER = 'data' # folder where the csv files are stored, relative to the current folder
petFile = 'data\Dutton.csv'
puppy_profile_file = 'data\PuppyProfiles.csv'
DOB = ''

#Read csv file
def load_file(csv_file=petFile):
    df = pd.read_csv(csv_file)
    print(df) # formatted, with leading index row

#Adds new row to file for new pet weight record
def add_new_record(pet_name):

    # asseble path from pet name and make sure the csv file exists
    csv_file = DATA_FOLDER + "/" + pet_name + '.csv'
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} does not exist.")
        return None
    
    df = pd.read_csv(csv_file)
    input_date = input("Input Date: ")
    weight = input("Input weight: ")
    image = input("Select Image: ")
    comment = input("Input comment: ")

    # create a new dataframe with a single row
    new_row = pd.DataFrame({'DateofEntry':[str(input_date)], 
                        "Weight":[int(weight)], 
                        "Image": [str(image)], 
                        'Comment':[str(comment)]}) 
    print(new_row)

    # append the new row to the dataframe using axis=0 to append row-wise
    # set ignore_index to True to force re-indexing of the appended rows
    # also, need to re-assign the dataframe to itself to capture the new rows
    df = pd.concat([df, new_row], axis=0, ignore_index=True) 
    print(df)
    
    # save the dataframe to the csv file
    df.to_csv(csv_file, index=False) # set index to False to avoid writing the index column

    return df # return the dataframe so we can use it later w/o having to reload it (

#Adds a new pet to file.
def add_new_pet(file=puppy_profile_file):
    """Information is entered by the user via keyboard and stores the new data in the csv file.
    For loop that will read through csv files and appends a new row. """
    """Information is entered by the user via keyboard and stores the new data in the csv file.
    For loop that will read through csv files and appends a new row."""
    pet_name = input("Input Pet's Name: ")
    DOB = input("Input pet's Date of Birth: ")
    breed = input("Input Breed: ")
    image = input("Input Image: " )

    # CH maybe eventually check if that pet already exists in the file?

    # Define the user data as a list
    user_data = [pet_name, DOB, breed, image]

    try:
        # Open the CSV file in append mode
        with open(file, mode='a', newline='') as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)
            
            # Write the user data to the CSV file
            writer.writerow(user_data)
            
        print("User data added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Returns every pet's record
def Get_All_Profiles(petProfile=puppy_profile_file):
    df = pd.read_csv(petProfile)
    print(df) # formatted, with leading index row
    '''Call Get_All_Unique_Pets() function
    Call Get_All_Info_For_Pet() function'''

#Prints out individual pet's entry records, e.g. an entry for a day
def print_indvidual_entry_record(csv_file=petFile):
    df = pd.read_csv(csv_file)
    userSearch = input("What record do you want to return?")
    r = df.loc[int(userSearch)]
    print(r, "\n")

#Returns individual pet's weight records
def print_weight_record_for_individual(csv_file=petFile):
    df = pd.read_csv(csv_file)
    userSearch = input("What weight do you wan to return?")

    r = df["Weight"].loc[int(userSearch)]
    #weight = df["Weight"].loc[r]
    #print({weight})
    print(r)

# gets dog's profile based on PetID.
def get_uniquedogprofile(pup=puppy_profile_file):
    '''returns dog's profiles based on petID.'''
    df = pd.read_csv(pup)
    userSearch = input("What pet's profile do you want to see? \n1. Dutton \n2. Kiko \n 3. Copper? Press Enter.")

    r = df["Weight"].loc[int(userSearch)]
    print(r, "\n")

#loads image
def get_image(pup=puppy_profile_file):
    df = pd.read_csv(pup)
    r = 2
    pupImage = df["Profile Image"].loc[r]
    # load and show images
    img = Image.open(pupImage)
    img.show() # external viewer

#Calculates age     
def getAge(pup=puppy_profile_file, csv_file=petFile): #DOB = '01/05/2023', , date_of_entry = '05/02/2023'
    """Calculate the age based on all of the Date fields from the PetRecord.csv file and compares to the DOB field from the pets.csv file."""
    df = pd.read_csv(pup)
    r = 1
    DOB = df["Date of Birth"].loc[r]
    print({DOB})

    df = pd.read_csv(csv_file)
    r = 1
    date_of_entry = df["DateofEntry"].loc[r]
    print({date_of_entry})   

    DOButc_time = time.strptime(DOB + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
    DOBepoch_time = timegm(DOButc_time)

    DOEutc_time = time.strptime(date_of_entry + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
    DOEepoch_time = timegm(DOEutc_time)

    #Print the age
    #Print(f"The person is "  + str(epoch_time) + " years old.")
    #print("UTC " + str(DOButc_time))
    #print("DOBepoch_time " + str(DOBepoch_time))
    #print("Month " + str(DOButc_time.tm_mon))
    #print("Day " + str(DOButc_time.tm_mday))
    #print("Year " + str(DOButc_time.tm_year))

    #Calculate the age
    age = DOEepoch_time - DOBepoch_time #Subtract the DateOfEntry = DateOfBirth
    #print("Age " + str(age))
    print("Days: " + str(age/(3600 * 24))) # ((60 seconds * 60 minutes) = 3600 * 24 hours)
    print("Months: " + str(age/(60 * 60 * 24 * 30))) # (60 seconds * 60 minutes * 24 hours * 30 days)
    print("Years: " + str(age/(3600 * 24 * 365))) # ((60 seconds * 60 minutes) = 3600 seconds * 24 hours * 365 days)

#Remove objects 
def remove_row():
    pass

#Plots csv file into plotly
def plotcsv():
    '''Plots pet csv file based on PetID selected by user. '''
    
# Get Pet
def display_UI():
    '''Print values per the unique PetIDs to generate buttons.'''


#get_image()
add_new_record("Dutton")  # better(?): just pass in the name of the pet, figure where the csv is in the function
load_file()
#getAge()
#print_indvidual_entry_record
#print_weight_record_for_individual()
#Get_All_Profiles()
#get_uniquedogprofile()
#add_new_pet()



