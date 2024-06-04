from tkinter import *
from tkinter.colorchooser import *

def mouseClick(event):
    global x1, y1
    x1 = event.x
    y1 = event.y

def drawRect(event):
    global x1, y1, x2, y2, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_rectangle(x1, y1, x2, y2, outline=penColor)

def colorSetting():
    global penColor
    color = askcolor()
    penColor = color[1]

def clearAll():
    canvas.delete("all")

x1, y1, x2, y2 = None,None,None,None
penColor = 'blue'

window = Tk()
window.title("사각형 그리기")
canvas = Canvas(window, width=300, height=400)
canvas.bind('<1>', mouseClick)
canvas.bind('<ButtonRelease-1>', drawRect)
canvas.pack()

p=PanedWindow(window)
p.pack()
btColor = Button(p, text="Color", command=colorSetting)
btClear = Button(p, text="clear", command=clearAll)
btColor.grid(row=0, padx=7, pady=10)
btClear.grid(row=0, column=1, pady=10)
window.mainloop()