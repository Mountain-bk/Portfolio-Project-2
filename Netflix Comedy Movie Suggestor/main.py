from tkinter import *

root = Tk()

canvas = Canvas(root, height="700", width="800", bg="#141414")
canvas.pack()

startButton = Button(root, text="start", padx="100", pady="50", bg="#E50914", fg="white")
startButton.pack()

root.mainloop()
