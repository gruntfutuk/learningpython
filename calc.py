# Calculator.py - tkinter calculator

from tkinter import *

# always inherit from Frame
class Calculator(Frame):

    # init will layout controls
    # and activate
    def __init__(self,parent=None):
        # always going to call Frame constructor
        Frame.__init__(self,parent)

        # "Screen" - an Entry
        self.entry = Entry(self)
        self.entry.grid(row=0,column=0,columnspan=4)

        # buttons - laid out in grid
        labels = "0123456789+-*/().%=C"

        for i in range(len(labels)):

            # local function - one for each button
            def cmd(key=labels[i]):   # default is label for each button
                # print(key)
                self.click(key)
                
            b = Button(self,command=cmd,text=labels[i],width=5,height=3)
            b.grid( row=i//4+1, column=i%4 )


    def click(self,key):
        print('click', key)

        # most keys just display add the key to the screen
        # except, =, which computes results and displays it
        # and C, which clears the screen

        if key=='=': # compute and display
            # get input, compute and display
            try:
                ans = eval( self.entry.get())
            except:
                ans = "ERROR"
            self.entry.delete(0,END)
            self.entry.insert(END,ans)
            
        elif key=='C': # clear display
            self.entry.delete(0,END)
        else:  # add key to display
            self.entry.insert(END,key)

Calculator().pack()
