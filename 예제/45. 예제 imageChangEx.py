from tkinter import *

def changeImage():
    img = PhotoImage(file="test.gif")
    imageLabel.configure(image=img)
    imageLabel.image = img
    photo=img

window = Tk()

photo = PhotoImage(file="test1.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

button = Button(window, text="이미지 변경", command=changeImage)
button.pack(pady=10)

window.mainloop()