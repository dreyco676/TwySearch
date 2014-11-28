from search import Search
from output import Output
from tkinter import *
class Application (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :
        #Search keyword
        self.instruction= Label(self,text="Enter Keyword")
        self.instruction.grid(row=0, column=0, columnspan=1, sticky=W)
        self.keyword = Entry(self)
        self.keyword.grid(row=0, column=1, columnspan=1, sticky=W)

        #Max Results
        self.max_result = Label(self,text="Enter Maximum Result")
        self.max_result.grid(row=1, column=0, columnspan=1, sticky=W)
        self.max_result2 = Entry(self)
        self.max_result2.grid(row=1, column=1, columnspan=1, sticky=W)

        #Execute search
        self.search_button = Button(self, text="Search", command=self.reveal)
        self.search_button.grid(row=2, column=0, sticky=W)

    def reveal(self):
        search = Search()
        search.keyword= self.keyword.get()
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
root.geometry("1024x768")
app = Application(root)
root.mainloop()







