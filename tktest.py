#Import the tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
from tkinter import Scrollbar

#Function Definition
def CurSelet(evt):
    value=str((Listbox1.get(ANCHOR)))
    messagebox.showinfo("Selection","You selected: " + str(value))

#Create a window
window=Tk()
#Change the Window Title
window.title("Example2-5")
#Change the dimension of the window
window.geometry("300x200")

#Add a label
Label1=Label(window, text="View the listbox and click on a number",justify=CENTER)
Label1.pack(side="top")

#Add the Frame for alignment and then
#the Listbox and Scrollbar widgets
Frame1=Frame(window)
Frame1.pack(side="top")
Listbox1 = Listbox(Frame1)
Listbox1.pack(side="left",fill=Y)

ScrollBar1=Scrollbar(Frame1,orient=VERTICAL)
ScrollBar1.config(command=Listbox1.yview)
ScrollBar1.pack(side=RIGHT,fill=Y)
Listbox1.yscrollcommand=ScrollBar1.set

#Populate the listbox with data
for i in range(20):
    Listbox1.insert(END, str(i))

Listbox1.bind("<<ListboxSelect>>", CurSelet) #Listbox Selection

window.mainloop()
