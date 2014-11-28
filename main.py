from search import TwitterSearch
from request import TwitterRequest
from output import FormatOutput
from auth import TwitterUser
from tkinter import *
class Application (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :
        self.instruction= Label(self,text="Enter Keyword")
        self.instruction.grid(row=0, column=0, columnspan=1, sticky=W)

        self.keyword = Entry(self)
        self.keyword.grid(row=0, column=1, columnspan=1, sticky=W)

        self.max_result = Label(self,text="Enter Maximum Result")
        self.max_result.grid(row=1, column=0, columnspan=1, sticky=W)

        self.max_result2 = Entry(self)
        self.max_result2.grid(row=1, column=1, columnspan=1, sticky=W)

        self.search_button = Button(self, text="Search", command=self.reveal)
        self.search_button.grid(row=2, column=0, sticky=W)

        #self.text= Text(self, width=70, height=40, wrap=WORD)
        #self.text.grid(row=3, column=0, columnspan=2, sticky=W)

        # self.download_button = Button(self, text="Download", command=self.download)
        # self.download_button.grid(row=2, column=2, sticky=W)

    def reveal(self):
        search = TwitterSearch()
        search.keyword= self.keyword.get()
        #print(self.max_result2.get())
        search.max_results =int(self.max_result2.get())


        req = TwitterRequest()
        req._req_param = search
        req._session_auth = auth
        data = req.make_request()
        save = FormatOutput()
        save._file_name = 'Output'
        save._out_type = 'tsv'
        save._result_set = data
        save.tsv_output()
        print("done")




#set user
user = TwitterUser()
user.read_json()
auth = user.auth()

root = Tk()
root.title("Twitter Search Downloader")
root.geometry("1024x768")
app = Application(root)
root.mainloop()







