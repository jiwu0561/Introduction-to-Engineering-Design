from tkinter import *

def inchCalculate():
    cm = float(cmE.get())
    inches = 0.394*cm
    incheE.insert(0, str(inches))

def cmCalculate():
    cm = float(incheE.get())/0.394
    cmE.insert(0, str(cm))
    
def clear_t():
    cmE.delete(0, END)
    incheE.delete(0, END)

window = Tk()
lab1=Label(window, text="센티미터", font=("돋음체", 14))
lab2=Label(window, text="인치", font=("돋음체", 14))
lab1.grid(row=0)
lab2.grid(row=1)

cmE = Entry(window, bg="pink", fg="black")
incheE = Entry(window, bg="pink", fg="black")
cmE.grid(row=0, column=1, padx=10, pady=5)
incheE.grid(row=1, column=1, padx=10, pady=5)

b1 = Button(window, text="cm→inches", command=inchCalculate)
b2 = Button(window, text="inches→cm", command=cmCalculate)
b3 = Button(window, text="clear",command=clear_t)

b1.grid(row=2, padx=10, pady=5)
b2.grid(row=2, column=1, padx=10, pady=5)
b3.grid(row=3, columnspan=2, pady=10)

window.mainloop()