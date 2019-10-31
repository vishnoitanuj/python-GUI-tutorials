from tkinter import *

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_windows()
    
    # Creation of init_windows
    def init_windows(self):
        
        #title of window
        self.master.title("GUI")

        #allow the widget to take the full space of the root widget
        self.pack(fill=BOTH, expand=1)

        #creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #create the file object
        file = Menu(menu)

        #adds a command to the menu option, calling it exit, and the command it runs on event is client_exit
        file.add_command(label="Exit",command=self.client_exit)

        #added file to our menu
        menu.add_cascade(label="File",menu=file)

        #create the file object
        edit = Menu(menu)

        #adds a command to the menu option, calling it undo.
        edit.add_command(label="Undo")

        #added edit to our menu
        menu.add_cascade(label="Edit",menu=edit)
        
    def client_exit(self):
        exit()

root = Tk()

#Size of the window
root.geometry("400x300")
app =Window(root)
root.mainloop()