from tkinter import *



def updateCallback(event):
    countOfLinks = countOfLinksEntry.get()
    q0 = q0Entry.get()
    qT = qTEntry.get()
    obstacle = obstacleEntry.get()
    print("countOfLinks = " + countOfLinks + "\nq0 = " + q0 + "\nqT = " + qT + "\nobstacle = " + obstacle + "\n")


inputWindow = Tk()
Label(inputWindow, text="Число звеньев").grid(row=1, column=1)
countOfLinksEntry = Entry(inputWindow)
countOfLinksEntry.grid(row=1, column=3)

Label(inputWindow, text="q->0").grid(row=2, column=1)
q0Entry = Entry(inputWindow)
q0Entry.grid(row=2, column=3)

Label(inputWindow, text="q->T").grid(row=3, column=1)
qTEntry = Entry(inputWindow)
qTEntry.grid(row=3, column=3)

Label(inputWindow, text="Информация о препятсвиях").grid(row=4, column=1)
obstacleEntry = Entry(inputWindow)
obstacleEntry.grid(row=4, column=3)

button = Button(inputWindow, text="Ok")
button.bind("<Button-1>", updateCallback)
button.grid(row=5, column=2)
