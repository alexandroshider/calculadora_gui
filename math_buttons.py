import tkinter as tk

class math_button:
    def __init__(self, window, math_operator=4):
        #self.button = tk.Tk()
        self.button = tk.Button(window, text = str(math_operator))
        self.button.pack()