from tkinter import *

class Pomodoro(Tk):
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Pomodoro App')
        self.root.config(padx=100, pady=50)
        self.root.mainloop()