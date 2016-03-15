from Tkinter import Tk, Frame, BOTH

class Example(Frame): #inherit from frame class
    def __init__(self,parent): #parent for parent class
        Frame.__init__(self,parent,background="lightgreen") #calling parent's class constructor
        self.parent=parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w=290
        h=150

        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()

        x = (sw-w)/2
        y = (sh-h)/2
        
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))

def main():
    root=Tk()
    app = Example(root)
    root.mainloop()

if __name__=='__main__':
    main()
