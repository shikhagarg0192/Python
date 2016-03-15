from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame,Style

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        style = Style()
        style.configure("TFrame", background="lightgreen")

        image1=Image.open("images.jpg")
        images = ImageTk.PhotoImage(image1)
        label1=Label(self, image = images)
        label1.image = images
        label1.place(x=20,y=20)

        image1=Image.open("images.jpg")
        images = ImageTk.PhotoImage(image1)
        label2=Label(self, image = images)
        label2.image = images
        label2.place(x=20,y=215)

        image1=Image.open("images.jpg")
        images = ImageTk.PhotoImage(image1)
        label3=Label(self, image = images)
        label3.image = images
        label3.place(x=280,y=20)

def main():
    root = Tk()
    root.geometry("600x600+300+300")
    app = Example(root)
    root.mainloop()

main()
