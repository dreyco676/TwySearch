from search import Search
from output import Output
from tkinter import *
from tkinter import messagebox

class Application (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :

        #Search keyword
        self.keyword_desc = Label(self,text="Enter Keyword")
        self.keyword_desc.grid(row=0, column=0, columnspan=1, sticky=W)
        self.keyword = Entry(self)
        self.keyword.grid(row=1, column=0, columnspan=1, sticky=W)

        #Platform
        self.platform_desc = Label(self,text="Select a platform")
        self.platform_desc.grid(row=0, column=2, columnspan=1, sticky=W)
        self.platform = Menubutton(text="Available Platforms")
        self.platform.menu = Menu(self.platform, tearoff=0)
        self.platform["menu"] = self.platform.menu
        twitter_var = IntVar()
        ebay_var = IntVar()
        self.platform.menu.add_checkbutton(label="Twitter",
                                  variable=twitter_var)
        self.platform.menu.add_checkbutton(label="Ebay",
                                  variable=ebay_var)
        self.platform.grid(row=1, column=2, columnspan=1, sticky=W)

        #ADVANCED OPTIONS
        self.advanced_opts_div = Label(self,text="ADVANCED OPTIONS")
        self.advanced_opts_div.grid(row=4, column=0, columnspan=3)

        #MAX_Results
        self.max_results_desc = Label(self,text="Maximum Results")
        self.max_results_desc.grid(row=7, column=0, columnspan=1, sticky=W)
        self.max_results = Entry(self)
        self.max_results.grid(row=8, column=0, columnspan=1, sticky=W)

        #Geocode
        self.geocode_desc = Label(self,text="Select Geocode")
        self.geocode_desc.grid(row=7, column=1, columnspan=1, sticky=W)
        self.geocode = Entry(self)
        self.geocode.grid(row=8, column=1, columnspan=1, sticky=W)

        #Lang
        self.lang_desc = Label(self,text="Select Language")
        self.lang_desc.grid(row=7, column=2, columnspan=1, sticky=W)
        self.lang = Entry(self)
        self.lang.grid(row=8, column=2, columnspan=1, sticky=W)

        #Result_type
        self.lang_desc = Label(self,text="Select Result Type")
        self.lang_desc.grid(row=9, column=0, columnspan=1, sticky=W)
        self.lang = Entry(self)
        self.lang.grid(row=10, column=0, columnspan=1, sticky=W)

        #Max Date
        self.max_date_desc = Label(self,text="Enter Max Date (YYYY-MM-DD)")
        self.max_date_desc.grid(row=9, column=1, columnspan=1, sticky=W)
        self.max_date = Entry(self)
        self.max_date.grid(row=10, column=1, columnspan=1, sticky=W)

        #output OPTIONS
        self.advanced_opts_div = Label(self,text="OUTPUT OPTIONS")
        self.advanced_opts_div.grid(row=13, column=0, columnspan=3)


        #File Name
        self.file_name_desc = Label(self,text="Enter Output File Name")
        self.file_name_desc.grid(row=16, column=2, columnspan=1, sticky=W)
        self.file_name = Entry(self)
        self.file_name.grid(row=17, column=2, columnspan=1, sticky=W)

        #Save Directory
        self.out_dir_desc = Label(self,text="Output Directory")
        self.out_dir_desc.grid(row=16, column=0, columnspan=1, sticky=W)
        self.out_dir = Entry(self)
        self.out_dir.grid(row=17, column=0, columnspan=1, sticky=W)

        #Output_type
        self.out_type_desc = Label(self,text="Select an Output Type")
        self.out_type_desc.grid(row=16, column=1, columnspan=1, sticky=W)
        self.out_type = Entry(self)
        self.out_type.grid(row=17, column=1, columnspan=1, sticky=W)


        #Execute search
        self.search_button = Button(self, text="Search", command=self.start_search)
        self.search_button.grid(row=20, column=0, columnspan=3)


    def start_search(self):
        search = Search()
        search.keyword = self.keyword.get()
        #print(self.max_result2.get())
        search.max_results =int(self.max_result2.get())
        search.platform = 'Twitter'

        data = search.make_request()
        save = Output()
        save.platform = search.platform
        save.file_name = 'Output'
        save.out_type = 'tsv'
        save.result_set = data
        save.format_output()
        print("done")

root = Tk()
root.title("Twitter Search Downloader")
root.geometry("800x600")
app = Application(root)
root.mainloop()







