from Tkinter import *
from PIL import Image, ImageTk
from ttk import Frame, Button, Style, Label

class Example(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def close_window():
        root.destroy()

    def initUI(self):
        self.parent.title("Buttons")
        self.style=Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        bard = Image.open("images.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(frame, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        
        self.pack(fill=BOTH, expand=1)
        closebutton = Button(self, text="Close")
        closebutton.pack(side=RIGHT, padx=5, pady=5)
        okbutton = Button(self, text="OK")
        okbutton.pack(side=RIGHT)

def main():
    root= Tk()
    root.geometry("400x300+300+300")
    app = Example(root)
    root.mainloop()

main()
