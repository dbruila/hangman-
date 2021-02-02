import random
from picture import *
from openFile import *
from string import ascii_lowercase
from StartPage import *
from rules import rules
from writeWords import *

buttons = {}


def newGame():
    start()
    global withSpaces
    global NumbGuesses
    global NumbWin
    global word
    global buttons

    NumbGuesses = 0
    NumbWin = 0
    word = random.choice(words)
    withSpaces = " ".join(word)
    lblWord.set(" ".join("_" * len(word)))

    n = 0
    for c in ascii_lowercase:
        btnAlf = Button(root, text=c, command=lambda c=c: guess(c), font=("Helvetica", "18"), width=4)
        btnAlf.grid(row=1 + (n // 9), column=1 + (n % 9))
        n += 1
        buttons[c] = btnAlf

    Button(root, text="New\nGame", command=lambda: newGame(), font=("Helvetica", "11")).grid(row=3, column=9,
                                                                                             sticky="NSWE")


def guess(letter):
    global NumbGuesses
    global NumbWin
    global buttons
    buttons.get(letter)["state"] = "disabled"
    if NumbGuesses < 8:
        txt = list(withSpaces)
        guessed = list(lblWord.get())
        if withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                    NumbWin += 1
                lblWord.set("".join(guessed))
                if NumbWin == len(word):
                    canvas.create_text(160, 250, text="You are win! ", fill="purple", font=("Helvetica", "18"))
        else:
            NumbGuesses += 1

            if NumbGuesses == 1:
                one()
            elif NumbGuesses == 2:
                two()
            elif NumbGuesses == 3:
                three()
            elif NumbGuesses == 4:
                four()
            elif NumbGuesses == 5:
                five()
            elif NumbGuesses == 6:
                six()
            elif NumbGuesses == 7:
                seven()
            elif NumbGuesses == 8:
                eight()
            root.update()
            if NumbGuesses == 8:
                canvas.create_text(160, 250, text="Game over!\n" + "Word is: " + word, fill="purple",
                                   font=("Helvetica", "18"))


lblWord = StringVar()

Label(root, textvariable=lblWord, font=("Helvetica", "18")).grid(row=0, column=1, columnspan=10, padx=10)

btnPlay = Button(root, text="Play", width=10, height=2, command=lambda: [btnPlay.destroy(), newGame()])
btnPlay.place(x=180, y=350)

btnWord = Button(root, text="Edit\nword's file", width=10, height=2, command=lambda: newWord())
btnWord.place(x=60, y=350)

btnRules = Button(root, text="Rules", width=10, height=2, command=lambda: rules())
btnRules.place(x=60, y=280)


root.mainloop()
