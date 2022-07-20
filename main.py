import tkinter as tk

window =  tk.Tk()
window.geometry('400x200')
greeting = tk.Label(text="Hello, mi bonita")
greeting.pack()

inputtxt = tk.Text(window,
                   height = 5,
                   width = 20)
inputtxt.pack()

boxes =  tk.Tk()
boxes.geometry('600x800')

inputtxt = tk.Text(window,
                   height = 8,
                   width = 20)
inputtxt.pack()
window.mainloop()
boxes.mainloop()