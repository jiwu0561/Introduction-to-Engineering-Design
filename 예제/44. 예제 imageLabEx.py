from tkinter import *

window = Tk()

photo = PhotoImage(file="fruit.gif")
imageLabel =Label(window, image=photo)
imageLabel.pack()

label = Label(window, text="fruit.gif 파일", font=("돋음체", 14, "bold"), fg="blue")
label.pack()

window.mainloop()