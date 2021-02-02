from mainWindow import *


def start():
    canvas.delete("all")


canvas.create_text(160, 50, text='To read the rules\nclick on the\nrules button.', fill="royalblue",
                   font=("Helvetica", "14"))
canvas.create_text(180, 120, text='To start the game\npress the play button.', fill="royalblue",
                   font=("Helvetica", "14"))
canvas.create_text(180, 200, text='To replace the words\nof the game with\nnew ones, click on\nthe button.',
                   fill="royalblue", font=("Helvetica", "14"))
