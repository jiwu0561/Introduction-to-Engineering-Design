from tkinter import *

window=Tk()
window.title("계산기")
window.geometry("320x110+100+100")

def calcute(event):
    label2["text"]="계산 결과 = "+str(eval(entry.get()))

label1 = Label(window, text="수식 (ex. 2*4-3)",font=("돋음체",12,"bold"))
label1.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(window)
entry.bind("<Return>", calcute)
entry.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(window, fg="blue", font=("돋음체",14,"bold"))
label2.grid(row=1, columnspan=2, pady=10)

window.mainloop()