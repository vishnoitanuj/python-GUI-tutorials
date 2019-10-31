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

        #creating a button instance
        quitButton = Button(self, text="Quit",command=self.client_exit)

        #Place the button on the window
        quitButton.place(x=0,y=0)

    def client_exit(self):
        exit()

root = Tk()

#Size of the window
root.geometry("400x300")
app =Window(root)
root.mainloop()