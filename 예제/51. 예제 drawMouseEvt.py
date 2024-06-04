from tkinter import *

def draw(event):
    global x, y
    can.create_line(x,y,event.x,event.y, fill=mycolor)
    x,y=event.x,event.y

def down(event):
    global x, y
    x,y=event.x,event.y

def up(event):
    global x, y
    if (x,y)==(event.x,event.y):
        can.create_line(x,y,x+1,y+1,fill=mycolor)

def change_b():
    global mycolor
    mycolor="blue"

w=Tk()
can = Canvas(w, width=500, height=500)
mycolor = "green"
can.bind('<B1-Motion>', draw)
can.bind('<ButtonPress>', down)
can.bind('<ButtonRelease>', up)
can.pack()
bt=Button(w, text="파랑색", command=change_b)
bt.pack(pady=10)
w.mainloop()