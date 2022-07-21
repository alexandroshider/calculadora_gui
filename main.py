import tkinter as tk

window =  tk.Tk()
window.geometry('400x200')
greeting = tk.Label(text="Hello, mi bonita")
greeting.pack()

#Box for writing text
inputtxt = tk.Text(window,
                   height = 5,
                   width = 20)
inputtxt.place(x=100,y=60)
#inputtxt.pack()
#number_1 = 

#button for clicking
okay = tk.Button(window, text = "okay")
okay.pack()

window.mainloop()