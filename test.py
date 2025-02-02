import tkinter as tk
from tkinter import Label
from tkinter import OptionMenu

root = tk.Tk()
root.title("Hypertension Info")
root.geometry("400x400")

clicked = tk.StringVar()

clicked.set("What is Hypertension?")
#def show():

    #myLabel = Label(root, text=clicked.get()).pack()

drop = OptionMenu(root, clicked, "According to the CDC, Hypertension is persistently high blood pressure at or above 130/80 mm Hg")

drop.pack()
root.mainloop()