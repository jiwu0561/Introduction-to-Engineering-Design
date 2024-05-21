from tkinter import *

def changeImage():
    global photo
    if photo["file"] == "test1.gif":
        path="test2.gif"
    else:
        path="test1.gif"
    img = PhotoImage(file=path)
    imageLabel.configure(image = img)
    imageLabel.image = img
    photo=img

window = Tk()

photo = PhotoImage(file="test1.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack(padx= 10, pady=10)

button = Button(window, text="이미지 변경", command=changeImage)
button.pack(pady=10)

window.mainloop()