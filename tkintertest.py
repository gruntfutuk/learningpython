#----------Finds the circumference of a circle ---------------

from tkinter import *

def roi():
   initialInvestmentGot = float(initialInvestment.get())
   interestRateGot = float(interestRate.get())
   yearsofinvestmentGot = float(yearsofinvestment.get())
   roi = initialInvestmentGot * (1 + (0.01 * interestRateGot))**yearsofinvestmentGot
   print(roi)
   roi = round(roi, 2)
   print("The return on investment is", roi)
   Label(master, text=f"ROI: {roi}").grid(row=3, column=3)

master = Tk()
Label(master, text="Initial Investment").grid(row=0)
Label(master, text="Iterest Rate").grid(row=1)
Label(master, text="Years of Investment").grid(row=2)
Label(master, text="% or decimal").grid(row=1, column=2)

initialInvestment = Entry(master)
initialInvestment.grid(row=0, column=1)
interestRate = Entry(master)
interestRate.grid(row=1, column=1)
yearsofinvestment = Entry(master)
yearsofinvestment.grid(row=2, column=1)
percentordec = Entry(master)
percentordec.grid(row=2, column=2)

Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=E, pady=4)
Button(master, text='Calculate', command=roi).grid(row=3, column=1, sticky=W, pady=4)

mainloop()