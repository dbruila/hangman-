from mainWindow import *


def one():
    canvas.create_line(100, 100, 100, 10, width=3, fill="midnightblue")
    canvas.create_line(100, 10, 200, 10, width=3, fill="midnightblue")
    canvas.create_line(200, 10, 200, 100, width=3, fill="midnightblue")
    canvas.create_line(200, 100, 100, 100, width=3, fill="midnightblue")
    root.update()


def two():
    canvas.create_line(110, 90, 110, 20, width=2, fill="black")
    canvas.create_line(110, 20, 190, 20, width=2, fill="black")
    canvas.create_line(190, 20, 190, 90, width=2, fill="black")
    canvas.create_line(190, 90, 110, 90, width=2, fill="black")
    root.update()


def three():
    canvas.create_line(130, 100, 130, 120, width=2, fill="black")
    canvas.create_line(170, 100, 170, 120, width=2, fill="black")
    canvas.create_line(170, 120, 130, 120, width=2, fill="black")
    root.update()


def four():
    canvas.create_line(130, 110, 120, 110, width=3, fill="black")
    canvas.create_line(120, 110, 120, 130, width=3, fill="black")
    canvas.create_line(180, 130, 180, 110, width=3, fill="black")
    canvas.create_line(180, 110, 170, 110, width=3, fill="black")
    root.update()


def five():
    canvas.create_line(80, 130, 230, 130, width=3, fill="black")
    canvas.create_line(80, 130, 110, 170, width=3, fill="black")
    canvas.create_line(110, 170, 260, 170, width=3, fill="black")
    canvas.create_line(230, 130, 260, 170, width=3, fill="black")
    root.update()


def six():
    canvas.create_line(100, 140, 220, 140, width=2, fill="midnightblue")

    canvas.create_line(100, 140, 120, 160, width=2, fill="midnightblue")
    canvas.create_line(120, 160, 240, 160, width=2, fill="midnightblue")

    canvas.create_line(220, 140, 240, 160, width=2, fill="midnightblue")

    canvas.create_line(106, 147, 227, 147, width=2, fill="midnightblue")
    canvas.create_line(115, 154, 233, 154, width=2, fill="midnightblue")
    root.update()


def seven():
    canvas.create_line(135, 40, 135, 60, width=5, fill="blueviolet")
    canvas.create_line(175, 40, 175, 60, width=5, fill="blueviolet")
    root.update()


def eight():
    canvas.create_line(130, 75, 180, 75, width=2, fill="black")
    canvas.create_line(130, 75, 130, 80, width=2, fill="black")
    canvas.create_line(180, 75, 180, 80, width=2, fill="black")
    root.update()
