
    def weight_entries_page(self):

        self.plotcsv()
        self.entries_page=Toplevel()
        self.read_path_location_from_csv()
        pupName = (self.df["Pets Name"].loc[int(self.clickedyou)])

        self.entries_page.title("Entries for pet: " + pupName)
        self.entries_page.geometry('800x800')
        self.entries_page.minsize(800,800)

        self.menu_frame = tk.Frame(self.entries_page)
        self.main_frame = tk.Frame(self.entries_page)

        self.menu_frame.place(x = 0, y = 0, relwidth= 0.3, relheight = 1)
        self.main_frame.place(relx = 0.3, y = 0, relwidth= 0.7, relheight = .5)

        self.menu_frame.columnconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')
        self.menu_frame.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')
        

        # weight photo
        self.menu_frame.label2 = tk.Label(self.menu_frame, image=self.photo)
        self.menu_frame.label2.grid(row=0, column=0, columnspan=10, rowspan=10, sticky = 'nw')

        self.main_frame.columnconfigure((0,1), weight = 1, uniform = 'a')
        self.main_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1, uniform = 'a')

        self.get_uniquedogprofile() 
        self.get_puppy_profile_image() # get's profile's image


 # gets dog's profile based on PetID. (Gets dog's profile)
    def get_uniquedogprofile(self):
        '''returns dog's profiles based on petID.'''
        self.getAgeforProfileInfo()
        puppyName = (self.df["Pets Name"].loc[int(self.clickedyou)])
        puppyDOB = (self.df["Date of Birth"].loc[int(self.clickedyou)])
        Breed = (self.df["Breed"].loc[int(self.clickedyou)])

        self.main_frame.label = tk.Label(self.main_frame, text='Profile:')
        self.main_frame.label.grid(row=6, column=1, padx=20, pady=10, sticky="ne")

        self.main_frame.label = tk.Label(self.main_frame, text='Name: ' + puppyName)
        self.main_frame.label.grid(row=7, column=1, padx=20, pady=10, sticky="ne")

        self.main_frame.label = tk.Label(self.main_frame, text='Date of Birth: ' + puppyDOB)
        self.main_frame.label.grid(row=8, column=1, padx=20, pady=10, sticky="ne")

        self.main_frame.label = tk.Label(self.main_frame, text='Current Age: ' + str(self.ageInMonths) + " months")
        self.main_frame.label.grid(row=9, column=1, padx=20, pady=10, sticky="ne")

        self.main_frame.label = tk.Label(self.main_frame, text='Breed: ' + Breed)
        self.main_frame.label.grid(row=10, column=1, padx=20, pady=10, sticky="ne")
        #self.entries_page .label = tk.Label(self.entries_page, text='Name: ' + puppyName + '\n Date of Birth: ' + puppyDOB + '\n Breed: ' + Breed)



    def get_puppy_profile_image(self):

        self.new_image_list = []

        puppyImage = (self.df["Profile Image"].loc[int(self.clickedyou)])

        img = Image.open(puppyImage)
        resized =  img.resize((325, 300)) #you should resize based on the aspect ratio / 2
        self.new_image_list.append(ImageTk.PhotoImage(resized))

        self.main_frame.label = tk.Label(self.main_frame, image=self.new_image_list)
        self.main_frame.label.grid(row=0, column=1, columnspan=5, rowspan=5, padx=10, pady=10, sticky="e")
        self.main_frame.label.grid

