import tkinter
from tkinter import messagebox

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="black", height=250, width=300)
coord = 100, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
top.mainloop()
