from tkinter import *

def click():
    str="이름: "+name.get()+", 학번: "+stNo.get()
    lab3["text"]=str

window = Tk()
window.geometry("220x200")
lab1=Label(window, text="이름")
lab2=Label(window, text="학번")
name=Entry(window)
name.insert(0, "홍길동")
stNo=Entry(window)
lab1.grid(row=0, padx=10, pady=10)
lab2.grid(row=1, padx=10, pady=10)
name.grid(row=0, column=1)
stNo.grid(row=1, column=1)
bt=Button(window, text="확인", bg="blue", fg="white", command=click)
bt.grid(row=2, padx=10, pady=10, columnspan=2)
lab3=Label(window, text="")
lab3.grid(row=3, padx=10, pady=10, columnspan=2)

window.mainloop()