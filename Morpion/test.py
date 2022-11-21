from tkinter import *
from tkinter import ttk

window = Tk()

def click_case(event):
    if event.x > 0 and event.x <100 and event.y < 100 and event.y > 0:
        return(50,50)
    if event.x > 0 and event.x <100 and event.y < 200 and event.y > 100:
        return(50,150)
    if event.x > 0 and event.x <100 and event.y < 300 and event.y > 200:
        return(50,250)

    if event.x > 100 and event.x <200 and event.y < 100 and event.y > 0:
        return(150,50)
    if event.x > 100 and event.x <200 and event.y < 200 and event.y > 100:
        return(150,150)
    if event.x > 100 and event.x <200 and event.y < 300 and event.y > 200:
       return(150,250)

    if event.x > 200 and event.x <300 and event.y < 100 and event.y > 0:
        return(250,50)
    if event.x > 200 and event.x <300 and event.y < 200 and event.y > 100:
        return(250,150)
    if event.x > 200 and event.x <300 and event.y < 300 and event.y > 200:
        return(250,250)

def place(symbol,coordonné):
    txt = canvas.create_text(coordonné[0], coordonné[1], text=symbol, font="Arial 30", fill="black")

window.geometry("300x300")

canvas = Canvas(window, width=300, height=300)

a=canvas.bind("<Button-1>",click_case)
print(a)

canvas.pack()

window.mainloop()