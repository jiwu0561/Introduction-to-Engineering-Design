from tkinter import *

def change_color(event):
    if event.char =='b':
        entry["bg"]="blue"
        entry["fg"]="white"

w = Tk()
w.title("Entry color Change")
w.geometry("300x300")

entry = Entry(w, width=30)
entry.pack(pady=20)
w.bind("<Key>", change_color)
w.mainloop()