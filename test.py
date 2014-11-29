from tkinter import *

root = Tk()

mb=  Menubutton(root, text="condiments", relief=RAISED )
mb.grid()
mb.menu  =  Menu( mb, tearoff=0 )
mb["menu"]  =  mb.menu

mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()
root.mainloop()
