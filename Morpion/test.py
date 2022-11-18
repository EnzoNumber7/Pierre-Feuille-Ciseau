from tkinter import *
from tkinter import ttk

root = Tk()


canvas = Canvas(root, width=300, height=300)

canvas.pack()

case1 = canvas.create_rectangle(0, 0, 100, 100)
case2 = canvas.create_rectangle(100, 0, 200, 100)
case3 = canvas.create_rectangle(200, 0, 300, 100)

case4 = canvas.create_rectangle(0, 100, 100, 200)
case5 = canvas.create_rectangle(100, 100, 200, 200)
case6 = canvas.create_rectangle(200, 100, 300, 200)

case7 = canvas.create_rectangle(0, 200, 100, 300)
case8 = canvas.create_rectangle(100, 200, 200, 300)
case9 = canvas.create_rectangle(200, 200, 300, 300)

Button(root, text ="pirate", relief=RAISED, cursor="pirate").pack()
root.mainloop()