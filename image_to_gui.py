from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    
    #Define setting upon initialization
    def __init__(self, master=None):

        #parameters that you want to send through the Frame class.
        Frame.__init__(self,master)

        #reference to master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #changing the title of our maste widget
        self.master.title("GUI")

        #allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #creating a menu instance
        menu=Menu(self.master)
        self.master.config(menu=menu)

        #create the file object
        file=Menu(menu)

        file.add_command(label="Exit",command=self.client_exit)

        menu.add_cascade(label="File",menu=file)

        edit=Menu(menu)
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        menu.add_cascade(label="Edit",menu=edit)
    
    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load.resize((60,40)))

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showText(self):
        text = Label(self, text="Hey there!")
        text.pack()
    
    def client_exit(self):
        exit()

# Root window creation
root = Tk()

# Set root geometry
root.geometry("400x300")

#Create instance
app = Window(root)

#mainloop
root.mainloop()