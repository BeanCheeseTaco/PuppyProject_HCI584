#!pip3 install pillow
import pandas as pd
import time
from calendar import timegm
from time import strftime
import datetime
from rapidfuzz import fuzz, process
from PIL import Image
import csv
# import dutton.csv and import PetRecord.csv
myfile = 'doc folder\dutton.csv'
DOB = ''

#Read file
def load_file(csv_file=myfile):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Process each row here
            print(row)

#Adds new row to file for new pet weight record
def add_new_record(file=myfile):
    """Information is entered by the user via keyboard and stores the new data in the csv file.
    For loop that will read through csv files and appends a new row."""
    input_date = input("Input Date: ")
    weight = input("Input weight: ")
    comment = input("Input weight: ")

    file = "doc folder\dutton.csv"

    # Define the user data as a list
    user_data = [input_date, weight, comment]

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

#Adds a new pet to file.
def add_new_pet(PetID, file):
    """Information is entered by the user via keyboard and stores the new data in the csv file.
    For loop that will read through csv files and appends a new row. """


#Plots csv file into plotly
def plotcsv():
    '''Plots pet csv file based on PetID selected by user. '''
    
# Get Pet
def display_UI():
    '''Print values per the unique PetIDs to generate buttons.'''

# Returns all unique pets.
def Get_All_Unique_Pets(PetData):
    '''Loop through file and finds the uniqueID and adds to an array. Returns the array of IDs.'''
    
# Returns all unique pet's info per petID (petData).
def Get_All_Info_For_Pet(PetID, PetData):
    '''Returns array with all info pertaining to petID (Parsed specific to the unique PetID.)'''

#Returns every pet's record
def Get_All_Info_For_All_Pets():
    '''Call Get_All_Unique_Pets() function
    Call Get_All_Info_For_Pet() function'''

    
#Prints out Pet's Records
def print_record_for_individual(PetID):
    '''Call Get_All_Info_For_Pet(PetID, PetData)
    Prints pet profile based on PetID selected by user from csv.'''
    
#Allow updates to Profile.
def updatedogprofile(PetID, PetProfile):
    '''returns updated pet's profile'''

# gets dog's profile based on PetID.
def get_dogprofile(PetID, PetProfile):
    '''returns dog's profiles based on petID.'''


#loads image
def get_image():
    # load and show images
    img = Image.open('doc folder\dogimage.jpg')
    # image parameters
    print(img.format, img.size, img.mode)
    display(img) # in jupyter, the image is shown as output


'''def load_file():
    with open('doc folder\dutton.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Process each row here
            print(row)
'''

# Calculates age     
def getAge(DOB = '01/04/2023', date_of_entry = '05/02/2023'):
    """Calculate the age based on all of the Date fields from the PetRecord.csv file and compares to the DOB field from the pets.csv file."""

    DOButc_time = time.strptime(DOB + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
    DOBepoch_time = timegm(DOButc_time)

    DOEutc_time = time.strptime(date_of_entry + ' 00:00:00', "%m/%d/%Y %H:%M:%S")
    DOEepoch_time = timegm(DOEutc_time)


    # Calculate the age
    #month = datetime.datetime.fromtimestamp(epoch_time).strftime('%m')
    month = DOButc_time.tm_mon
    day = DOButc_time.tm_mday
    year = DOButc_time.tm_year

    # Print the age
    #print(f"The person is "  + str(epoch_time) + " years old.")
    print("UTC " + str(DOButc_time))
    print("Month " + str(month))
    print("Day " + str(day))
    print("Year " + str(year))

    # Calculate the age



#get_image()
#add_new_record(myfile)
load_file()
getAge()