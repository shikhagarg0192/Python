from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI(parent)
        
    def initUI(self,parent):
        self.parent.title("Quit Button")
        self.style= Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH,expand=1)
        quitbutton=Button(self,text="Quit",command=parent.destroy)
        quitbutton.place(x=50,y=50)
       
def main():
    root=Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

main()
