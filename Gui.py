__author__ = 'apple'

from Tkinter import *
class Application (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

        def create_widgets(self) :
            self.instruction= Label(self,text="Enter Keyword")
            self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

            self.keyword = Entry(self)
            self.Keyword.grid(row=0, column=1, columnspan=2, sticky=W)

            self.geocode = Label(self,text="Enter geocode")
            self.geocode.grid(row=1, column=0, columnspan=2, sticky=W)

            self.geocode2 = Entry(self)
            self.geocode2.grid(row=1, column=0, columnspan=2, sticky=W)

            self.search_button = Button(self, text="Search", command=self.reveal)
            self.search_button.grid(row=2, column=0, sticky=W)

            self.text=Text(self, width=35, height=5, wrap=WORD)
            self.text.grid(row=3, column=0, columnspan=2, sticky=W)

            self.download_button = Button(self, text="Download", command=self.download)
            self.download_button.grid(row=2, column=2, sticky=W)

            #def reveal(self):
                #search
        #self.text.insert(0.0,output)

        #def download
        self.root = self.tk()
        self.root.title("Twitter Search Downloader")
        self.root.geometry("500x250")
        self.app = Application(self.root)
        self.root.mainloop()






