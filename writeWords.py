from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def newWord():
    root = Tk()
    root.title("Edit word's file")
    root.geometry("400x500")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    textWarn1 ="\nTo start the game with new words, start\n the game again."
    textWarn = "To change words in the file:\n1. click 'open file'\n2. add / delete / edit words in the file\n3. PLEASE NOTE THAT WORDS\nSHOULD BE WRITTEN ONE UNDER\nONE WITHOUT SPACES, COMMA,\nDOTS, etc.\n4. check the changes and click 'save file'"
    my_text1 = Text(root, width=33, height=10, font=("Helvetica", "12"))
    my_text1.pack(pady=10)
    my_text1.insert(END, textWarn)
    my_text1.tag_add("start", "4.0", "8.0")
    my_text1.tag_config("start", foreground="red")
    my_text1.insert(END, textWarn1)
    my_text1.tag_add("start", "9.0", "11.0")
    my_text1.tag_config("start", foreground="red")

    my_text = Text(root, width=33, height=12, font=("Helvetica", "12"))
    my_text.pack(pady=10)

    my_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=my_text.yview)

    btnOpen = Button(root, text="Open\nfile", width=10, height=2, command=lambda: [openF()])
    btnOpen.place(x=90, y=450)
    btnSave = Button(root, text="Save\nfile", width=10, height=2, command=lambda: saveChang())
    btnSave.place(x=210, y=450)

    def openF():
        text_file = open("dict\words.txt", "r")
        stuff = text_file.read()

        my_text.delete('1.0', END)
        my_text.insert(END, stuff)
        text_file.close()

    def saveF():
        text_file = open("dict\words.txt", "w")
        text_file.write(my_text.get(1.0, END))

    def saveChang():
        global reload
        MsgBox = messagebox.askquestion('Save changes', 'Are you sure you want to save the changes?')
        if MsgBox == 'yes':
            saveF()
            restart_program()
        else:
            tk.messagebox.showinfo('Changes ',' Changes not saved!')
