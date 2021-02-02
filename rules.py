from tkinter import *

label = None

with open("dict/rules.txt", "r") as file:
    rul = file.read()


def rules():
    global label
    root = Tk()
    root.title("Rules")
    label = Label(root, text=rul, font=("Helvetica", "16"), fg="royalblue")
    label.pack()
