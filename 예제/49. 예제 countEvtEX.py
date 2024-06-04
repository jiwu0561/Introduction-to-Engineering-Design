from tkinter import *

window = Tk()
window.title("카운트")
window.geometry("250x300+100+100")

count=0

def countUp():
    global count
    count += 1
    label2.config(text=str(count))


photo = PhotoImage(file="test.gif")
imageLabel = Label(window, image=photo)

imageLabel.grid(row=0, columnspan=2, padx=20, pady=20)

label1=Label(window, text="그림 조회수: ", font=("돋음체",12,"bold"))
label1.grid(row=1, column=0, padx=10, pady=10)

label2 = Label(window, text="0", font=("돋음체",12,"bold"))
label2.grid(row=1, column=1, pady=10)

button = Button(window, text="조회", width=15, command=countUp)
button.grid(row=2, columnspan=2, padx=10, pady=10)

window.mainloop()