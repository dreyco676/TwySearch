from search import Search
from output import Output
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

class SearchDownloader (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :

        #Search keyword
        self.keyword_desc = Label(self,text="Enter Keyword")
        self.keyword_desc.grid(row=0, column=0, columnspan=1)
        self.keyword = Entry(self)
        self.keyword.grid(row=1, column=0, columnspan=1)

        #Platform
        self.platform_desc = Label(self,text="Select a platform")
        self.platform_desc.grid(row=0, column=2, columnspan=1)
        platform_options = ['Twitter']
        self.platform_v = StringVar()
        self.platform_v.set(platform_options[0])
        self.platform_om = OptionMenu(self, self.platform_v, *platform_options)
        self.platform_om.grid(row=1, column=2, columnspan=1)

        #Divider
        self.div1 = Label(self,text="____________________________________________________________________")
        self.div1.grid(row=3, column=0, columnspan=3)

        #ADVANCED OPTIONS
        self.advanced_opts_div = Label(self,text="ADVANCED OPTIONS")
        self.advanced_opts_div.grid(row=4, column=0, columnspan=3)
        #Divider
        self.div2 = Label(self,text="____________________________________________________________________")
        self.div2.grid(row=5, column=0, columnspan=3)

        #MAX_Results
        self.max_results_desc = Label(self,text="Maximum Results")
        self.max_results_desc.grid(row=7, column=0, columnspan=1)
        self.max_results = Entry(self)
        self.max_results.grid(row=8, column=0, columnspan=1)

        #Geocode
        #(latitude,longitude,radius[mi/km])
        self.geocode_desc = Label(self,text="Enter Geocode")
        self.geocode_desc.grid(row=7, column=1, columnspan=1)
        self.geocode = Entry(self)
        self.geocode.grid(row=8, column=1, columnspan=1)

        #Lang
        #use 639-1 language codes
        #picked top languages http://www.statista.com/statistics/267129/most-used-languages-on-twitter/
        self.lang_desc = Label(self,text="Select Language")
        self.lang_desc.grid(row=7, column=2, columnspan=1)
        self.lang_options = {'None':'None','Arabic':'ar', 'Dutch':'nl', 'English':'en', 'Japanese':'ja', 'Korean':'ko',
                        'Portuguese':'pt', 'Spanish':'es', 'Malay':'ms', 'Thai':'th'}
        self.lang_v = StringVar()
        self.lang_v.set(self.lang_options['None'])
        self.lang_om = OptionMenu(self, self.lang_v, *self.lang_options)
        self.lang_om.grid(row=8, column=2, columnspan=1)

        #Result_type
        self.result_type_desc = Label(self,text="Select Result Type")
        self.result_type_desc.grid(row=9, column=0, columnspan=1)
        result_type_options = ['Mixed','Recent','Popular']
        self.result_type_v = StringVar()
        self.result_type_v.set(result_type_options[0])
        self.result_type_om = OptionMenu(self, self.result_type_v, *result_type_options)
        self.result_type_om.grid(row=10, column=0, columnspan=1)

        #Max Date
        #(YYYY-MM-DD)
        self.max_date_desc = Label(self,text="Enter Max Date")
        self.max_date_desc.grid(row=9, column=2, columnspan=1)
        self.max_date = Entry(self)
        self.max_date.grid(row=10, column=2, columnspan=1)

        #Divider
        self.div3 = Label(self,text="____________________________________________________________________")
        self.div3.grid(row=11, column=0, columnspan=3)

        #File Name
        self.file_name = Button(self, text="Save as...", command=self.save_as)
        self.file_name.grid(row=12, column=0, columnspan=1)

        #Execute search
        self.search_button = Button(self, text="Search", command=self.start_search)
        self.search_button.grid(row=12, column=2, columnspan=1)

    def save_as(self):
        self.file_opt = options = {}
        options['filetypes'] = [('JSON', '.json'), ('Tab Seperated', '.tsv')]
        options['initialfile'] = 'myfile.json'
        options['parent'] = root
        file = filedialog.asksaveasfilename(**self.file_opt)
        self.file_name = file
        self.file_type = os.path.splitext(file)[1]

    def start_search(self):
        search = Search()
        #set values for search from GUI
        search.keyword = self.keyword.get()
        search.platform = self.platform_v.get()
        search.max_results = self.max_results.get()
        search.geocode = self.geocode.get()
        search.lang = self.lang_options[self.lang_v.get()]
        search.result_type = self.result_type_v.get()
        search.max_date = self.max_date.get()
        messagebox.showinfo("Estimated Time to Complete", str(search.estimate_request_time()) + ' Seconds')

        data = search.make_request()
        save = Output()
        #set values from GUI
        save.platform = search.platform
        save.file_name = self.file_name
        save.out_type = self.file_type
        save.result_set = data
        save.format_output()
        messagebox.showinfo("Completed", "Search Completed")

root = Tk()
root.title("Twitter Search Downloader")
root.geometry("450x275")
app = Application(root)
root.mainloop()







