# Credit: https://www.python-course.eu/tkinter_canvas.php
# try:
#     import Tkinter as tk     # Python 2.x
# except ImportError:
#     import tkinter as tk     # Python 3.x

# import tkinter as tk
from tkinter import *
# import random

FONT15 = ('Arial', 15)
FONT32 = ('Arial', 32)

BGB = 'black'
BGY = 'yellow'
BGW = 'white'
FGG = 'green'
FGY = 'yellow'
FGB = 'black'
FGBL = 'blue'
#
# trivia_window = tk.Tk()
# trivia_window.title('WELCOME TO THE TRIVIA MAZE GAME')
# trivia_window_width = 1100
# trivia_window_height = 1100
# trivia_canvas = tk.Canvas(master=trivia_window,
#                           width=trivia_window_width,
#                           height=trivia_window_height,
#                           background=BGB)
#
# player_image = tk.PhotoImage(master=trivia_canvas, file="Rick.PNG")
# exit_image = tk.PhotoImage(master=trivia_canvas, file="ExitDoor.png")


class TriviaMazeGUI:

    def __init__(self, rows, cols, master=None):
        self.master = master

        self.__rows = rows
        self.__cols = cols
        # room size
        self.__col_width = 100
        self.__row_height = 100

        # space between room
        self.__row_blank_space = 30
        self.__col_blank_space = 30

        # keep player location
        self.__player_row = 0
        self.__player_col = 0

        self.trivia_canvas = Canvas(master, width=800, height=700)

        self.player_image = PhotoImage(master=self.trivia_canvas, file="Rick.PNG")
        self.exit_image = PhotoImage(master=self.trivia_canvas, file="ExitDoor.png")

        self.create_maze()
        self.create_player(0, 0)
        self.create_exit(self.__rows-1, self.__cols - 1)

        master.bind("<Left>", master.left)
        master.bind("<Right>", master.right)
        master.bind("<Up>", master.up)
        master.bind("<Down>", master.down)

        self.trivia_canvas.pack()

    def create_player(self, i, j):
        col = j * self.__col_width + self.__col_blank_space + self.__col_width / 5
        row = i * self.__row_height + self.__row_blank_space + self.__row_height / 8
        return self.trivia_canvas.create_image(col,
                                               row,
                                               anchor=NW,
                                               image=self.player_image)

    def create_exit(self, i, j):
        col = j * self.__col_width + self.__col_blank_space + self.__col_width / 12
        row = i * self.__row_height + self.__row_blank_space + self.__row_height / 10
        return self.trivia_canvas.create_image(col,
                                               row,
                                               anchor=NW,
                                               image=self.exit_image)

    def create_maze(self):

        for row in range(0, self.__rows):
            for col in range(0, self.__cols):

                self.trivia_canvas.create_rectangle(col * self.__col_width + self.__col_blank_space,
                                               row * self.__row_height + self.__row_blank_space,
                                               (col+1) * self.__col_width,
                                               (row+1) * self.__row_height,
                                               fill="yellow")
            self.trivia_canvas.pack()
            self.trivia_canvas.update()

    def movement(self):
        self.trivia_canvas.move((self.player_image, self.__player_row, self.__player_col))
        self.trivia_canvas.after(100, self.movement)

    def right(self, event):
        self.__player_col += 1
        self.trivia_canvas.move(self.player_image, self.__player_row, self.__player_col)

    def left(self, event):
        self.__player_col -= 1
        self.trivia_canvas.move(self.player_image, self.__player_row, self.__player_col)

    def up(self, event):
        self.__player_row += 1
        self.trivia_canvas.move(self.player_image, self.__player_row, self.__player_col)

    def down(self, event):
        self.__player_row -= 1
        self.trivia_canvas.move(self.player_image, self.__player_row, self.__player_col)


if __name__ == "__main__":
    master = Tk()
    trivia = TriviaMazeGUI(4, 5, master)

    master.bind("<Left>", trivia.left)
    master.bind("<Right>", trivia.right)
    master.bind("<Up>", trivia.up)
    master.bind("<Down>", trivia.down)

    mainloop()






