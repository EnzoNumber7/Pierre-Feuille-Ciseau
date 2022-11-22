import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        python_image = tk.PhotoImage(file='/img/croix.png')
        ttk.Label(self, image=python_image).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()