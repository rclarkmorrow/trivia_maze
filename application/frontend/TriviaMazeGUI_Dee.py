# Credit: https://www.python-course.eu/tkinter_canvas.php

import tkinter as tk
import random

FONT15 = ('Arial', 15)
FONT32 = ('Arial', 32)

BGB = 'black'
BGY = 'yellow'
BGW = 'white'
FGG = 'green'
FGY = 'yellow'
FGB = 'black'
FGBL = 'blue'

trivia_window = tk.Tk()
trivia_window.title('WELCOME TO THE TRIVIA MAZE GAME')
trivia_window_width = 1100
trivia_window_height = 1100
trivia_canvas = tk.Canvas(master=trivia_window,
                          width=trivia_window_width,
                          height=trivia_window_height,
                          background=BGB)
player_image = tk.PhotoImage(master=trivia_canvas, file="Rick.PNG")
exit_image = tk.PhotoImage(master=trivia_canvas, file="ExitDoor.png")


class TriviaMazeGUI:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        # room size
        self.__col_width = 100
        self.__row_height = 100

        # space between room
        self.__row_blank_space = 30
        self.__col_blank_space = 30

    def create_player(self, i, j):
        col = j * self.__col_width + self.__col_blank_space + self.__col_width / 5
        row = i * self.__row_height + self.__row_blank_space + self.__row_height / 8
        return trivia_canvas.create_image(col,
                                          row,
                                          anchor=tk.NW,
                                          image=player_image)

    def create_exit(self, i, j):
        col = j * self.__col_width + self.__col_blank_space + self.__col_width / 12
        row = i * self.__row_height + self.__row_blank_space + self.__row_height / 10
        return trivia_canvas.create_image(col,
                                          row,
                                          anchor=tk.NW,
                                          image=exit_image)

    def create_maze(self):

        for row in range(0, self.__rows):
            for col in range(0, self.__cols):

                trivia_canvas.create_rectangle(col * self.__col_width + self.__col_blank_space,
                                               row * self.__row_height + self.__row_blank_space,
                                               (col+1) * self.__col_width,
                                               (row+1) * self.__row_height,
                                               fill="yellow")
            trivia_canvas.pack()
            trivia_canvas.update()

        # randomly generate Entrance(i) and Exit(o) for the maze
        en_row = random.randint(0, self.__rows - 1)
        en_col = random.randint(0, self.__cols - 1)
        ex_row = random.randint(0, self.__rows - 1)
        ex_col = random.randint(0, self.__cols - 1)
        # check if the entrance row = exit row, 'Yes" assign entrance row = 0, exit row = row - 1
        if en_row == ex_row:
            en_row = 0
            ex_row = self.__rows - 1

        self.create_player(en_row, en_col)
        self.create_exit(ex_row, ex_col)

        trivia_window.mainloop()

    def create_content(self, i, j, content):
        """
        Create content such as Entrance, Exit, Player etc at a specified Index of the room.
        """
        trivia_canvas.create_text(j * self.__col_width + self.__col_blank_space + self.__col_width / 3,
                                  i * self.__row_height + self.__row_blank_space + self.__row_height / 3,
                                  text=content,
                                  font=FONT15,
                                  fill=FGB)

    def main(self):
        maze = TriviaMazeGUI(4, 5)
        maze.create_maze()


if __name__ == "__main__":
    trivia = TriviaMazeGUI(4, 5)
    trivia.main()




