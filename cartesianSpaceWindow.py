from tkinter import *

carcesianSpacceWindow = Tk()
carcesianSpacceWindow.resizable(width=False, height=False)

canvas = Canvas(carcesianSpacceWindow, height=600, width=600)
canvas.pack()

abscissa = canvas.create_line(0, 300, 600, 300, fill="red")
ordinate = canvas.create_line(300, 0, 300, 600, fill="red")

def putDot(x,y):
    dot = canvas.create_oval(x, y, x, y, fill="blue")

putDot(200,500)