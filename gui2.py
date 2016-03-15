from Tkinter import Tk, Frame, BOTH

class Example(Frame): #inherit from frame class
    def __init__(self,parent): #parent for parent class
        Frame.__init__(self,parent,background="lightgreen") #calling parent's class constructor
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.parent.title("simple")
        self.pack(fill=BOTH,expand=1)

def main():
    root=Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__=='__main__':
    main()
