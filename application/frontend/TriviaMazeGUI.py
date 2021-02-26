
from tkinter import *
import tkinter as tk
import random
from Player import Player
from Maze import Maze
from TrivaiMaze import TriviaMaze


FONT15 = ('Arial', 15)
FONT32 = ('Arial', 32)

BGB = 'black'
BGY = 'yellow'
BGW = 'white'
FGG = 'green'
FGY = 'yellow'
FGB = 'black'
FGBL = 'blue'


class TriviaMazeGUI(object):

    def __init__(self, num_rows, num_cols):
        """
        Initialization of the variables
        """
        global n_rows, n_cols, row_blank_space, col_blank_space, player, hit_point, pillar_collected, \
            healing_potion_count, vision_potion_count
        """
        Initializing Number of Rows and Columns of the Dungeon maze
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        n_rows = num_rows
        n_cols = num_cols

        """
        Initializing the room sizes
        """
        self.col_width = 100
        self.row_height = 100

        """
        Initializing spacing between rooms
        """
        row_blank_space = 30
        col_blank_space = 30

        """
        Score Card Initialisation
        """
        player = Player(" ")
        hit_point = player.hit_points
        pillar_collected = player.pillar_collected
        healing_potion_count = player.healing_potion_count
        vision_potion_count = player.vision_potion_count


    def create_tk_windows(self):
        """
        Creates tk windows and canvas
        """
        global my_window, my_canvas, adventurer_image, window_width, window_height
        """
        Creating a window and canvas
        """
        my_window = tk.Tk()
        my_window.title('WELCOME TO THE TRIVIA MAZE GAME')
        window_width = 1100
        window_height = 1100
        my_canvas = tk.Canvas(master=my_window, width=window_height, height=window_height, background=BGB)
        adventurer_image = PhotoImage(master=my_canvas, file="PlayerImg.png")

        """
        Binding the key board strokes with GUI
        """
        my_window.bind("<Left>", TriviaMazeGUI.left)
        my_window.bind("<Right>", TriviaMazeGUI.right)
        my_window.bind("<Up>", TriviaMazeGUI.up)
        my_window.bind("<Down>", TriviaMazeGUI.down)

    def create_rooms(self):
        """
        The method creates rooms on canvas
        """
        global my_canvas

        for i in range(0, self.num_rows):
            for j in range(0, self.num_rows):
                my_canvas.create_rectangle(j * self.col_width + col_blank_space,
                                           i * self.row_height + row_blank_space,
                                           (j+1) * self.col_width,
                                           (i+1) * self.row_height,
                                           fill="yellow")
            my_canvas.pack()
            my_canvas.update()

    def create_content(self, i, j, content):
        """
        Create content such as Pillar, Pit etc at a specified Index of the room.
        """
        my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                              i * self.row_height + row_blank_space + self.row_height / 3,
                              text=content,
                              font=FONT15,
                              fill=FGBL)
        # if content == 'A' or content == 'E' or content == 'E' or content == 'P' or content == 'I':
        #     my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
        #                           i * self.row_height + row_blank_space + self.row_height / 3,
        #                           text=content,
        #                           font=FONT15,
        #                           fill=FGBL)
        # else:
        #     my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
        #                           i * self.row_height + row_blank_space + self.row_height / 3,
        #                           text=content,
        #                           font=FONT15,
        #                           fill=FGBL)

    def create_north_door(self, i, j, north_door_symbol):
        """
        Creates north door for a room
        """
        if north_door_symbol == '-':
            my_canvas.create_rectangle(j*self.col_width+50,
                                       i*self.row_height+20,
                                       j*self.col_width+80,
                                       i*self.row_height+30,
                                       fill=FGG)
            my_canvas.pack()
            my_canvas.update()

    def create_south_door(self, i, j, south_door_symbol):
        """
        Creates south door for a room
        """
        if south_door_symbol == '-':
            my_canvas.create_rectangle(j*self.col_width+50,
                                       i*self.row_height+110,
                                       j*self.col_width+80,
                                       i*self.row_height+100,
                                       fill=FGG)
            my_canvas.pack()
            my_canvas.update()

    def create_east_door(self, i, j, east_door_symbol):
        """
        Creates east door for a room
        """
        if east_door_symbol == '|':
            my_canvas.create_rectangle(j*self.col_width+10+self.col_width,
                                       i*self.row_height+80,
                                       (j+1)*self.col_width,
                                       (i+1)*self.row_height-self.row_height/2,
                                       fill=FGG)
        my_canvas.pack()
        my_canvas.update()

    def create_west_door(self, i, j, west_door_symbol):
        """
        Creates west door for a room
        """
        if west_door_symbol == '|':
            my_canvas.create_rectangle(j*self.col_width+20,
                                       i*self.row_height+50,
                                       j*self.col_width+30,
                                       i*self.row_height+80,
                                       fill=FGG)
        my_canvas.pack()
        my_canvas.update()

    def create_adventurer(self, i, j):
        """
        Creates adventurers on canvas
        """
        return my_canvas.create_image(i, j, anchor=NW, image=adventurer_image)

    def left(event):
        """
        Event Handling Method for LEFT keystroke movements
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols,\
            player, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index
        next_i = adventurer_i_index

        if event.keysym == 'Left':
            adventurer_j_index = adventurer_j_index-1
            next_j=adventurer_j_index
            TriviaMazeGUI.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if TriviaMaze.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
            x = -100 # Keep this same as 'self.col_width'
            y = 0
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_j_index = adventurer_j_index + 1  # This takes care of repeated key press

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 3500, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(player.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            label_pillars = tk.Label(my_window, text="Pillars Collected: " + str(player.pillar_collected))
            label_pillars.config(font=FONT15)
            my_canvas.create_window(950, 425, window=label_pillars)
            return

    def right(event):
        """
        Event Handling Method for RIGHT key stroke movements
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols,\
            player, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion
        curr_i = adventurer_i_index
        curr_j = adventurer_j_index
        next_i = adventurer_i_index

        if event.keysym == 'Right':
            adventurer_j_index = adventurer_j_index + 1
            next_j = adventurer_j_index
            TriviaMazeGUI.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if TriviaMaze.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
            x = 100
            y = 0
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_j_index = adventurer_j_index - 1

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(player.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            label_pillars = tk.Label(my_window, text="Pillars Collected: " + str(player.pillar_collected))
            label_pillars.config(font=FONT15)
            my_canvas.create_window(950, 425, window=label_pillars)
            return

    def up(event):
        """
        Event Handling Method to create UP key stroke movements
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols, \
            player, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index

        next_j = adventurer_j_index
        if event.keysym == 'Up':
            adventurer_i_index = adventurer_i_index-1
            next_i = adventurer_i_index
            TriviaMazeGUI.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if TriviaMaze.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
            x = 0
            y = -100  # Keep this same as self.row_height
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_i_index = adventurer_i_index + 1

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(player.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            label_pillars = tk.Label(my_window, text="Pillars Collected: " + str(player.pillar_collected))
            label_pillars.config(font=FONT15)
            my_canvas.create_window(950, 425, window=label_pillars)
            return

    def down(event):
        """
        Event Handling Method to create DOWN keystroke movement
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, \
            player, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index

        next_j = adventurer_j_index
        if event.keysym == 'Down':
            adventurer_i_index = adventurer_i_index+1
            next_i = adventurer_i_index
            TriviaMazeGUI.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if TriviaMaze.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
            x = 0
            y = 100
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_i_index = adventurer_i_index - 1

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!")
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!")
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(player.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            label_pillars = tk.Label(my_window, text="Pillars Collected: " + str(player.pillar_collected))
            label_pillars.config(font=FONT15)
            my_canvas.create_window(950, 425, window=label_pillars)
            return

    def score_card(maze, curr_x, curr_y, next_x, next_y, column_count, row_count):
        """
        Generates score card such as hit points, pillars collected
        """
        global player, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        if TriviaMaze.if_passable(maze, curr_x, curr_y, next_x, next_y, column_count, row_count):
            next_room = maze.room_list[next_x][next_y]
            curr_room = next_room
            if hit_point < 0:
                print("You have lost all the hit points.")
                return
            if curr_room.room_content == "X":
                pit_point = random.randint(1, 20)
                hit_point = hit_point - pit_point
                curr_room.room_content = " "
            elif curr_room.room_content == "H":
                healing_point = random.randint(1, 40)
                hit_point = hit_point + healing_point
                healing_potion_count += 1
                curr_room.room_content = " "
            elif curr_room.room_content == "A" or curr_room.room_content == "E" or curr_room.room_content == "I" or \
                curr_room.room_content == "P":
                pillar_collected.append(curr_room.room_content)
                curr_room.room_content = " "
            elif curr_room.room_content == "V":
                vision_potion_count += 1
            player.hit_points = hit_point
            return

    def main(self):
        """
        This is the main method and Entry point for the program.
        """
        global my_image, adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols
        adventurer_i_index = 0
        adventurer_j_index = 0

        # Create tk windows and bind key strokes
        TriviaMazeGUI.create_tk_windows(self)

        # Create GUI rooms
        dungeon = TriviaMazeGUI(n_rows, n_cols)
        dungeon.create_rooms()

        # Populate the GUI rooms with dungeon content
        dng = Maze(n_rows, n_cols)
        dng.dungeon_generator()
        print(dng)
        for i in range(0, n_rows):
            for j in range(0, n_cols):
                row_index = i
                col_index = j
                content = dng.room_list[i][j].room_content
                dungeon.create_content(row_index, col_index, content)

                east_door_symbol = dng.room_list[i][j].room_matrix[1][2]
                dungeon.create_east_door(row_index, col_index, '|')

                west_door_symbol = dng.room_list[i][j].room_matrix[1][0]
                dungeon.create_west_door(row_index, col_index, '|')

                north_door_symbol = dng.room_list[i][j].room_matrix[0][1]
                dungeon.create_north_door(row_index, col_index, '-')

                south_door_symbol = dng.room_list[i][j].room_matrix[2][1]
                dungeon.create_south_door(row_index, col_index, '-')

                if content == 'i':
                    adventurer_i_index = i
                    adventurer_j_index = j
                    my_image = dungeon.create_adventurer(adventurer_j_index*100+32, adventurer_i_index*100+32)

                if content == 'O':
                    exit_i_index = i
                    exit_j_index = j

        """
         Displays
        """
        # label1a = tk.Label(my_window, text='INSTRUCTIONS:')
        # label1a.config(font=FONT15)
        # my_canvas.create_window(950, 50, window=label1a)
        #
        # label1b = tk.Label(my_window, text='Use Keyboard Arrow Keys')
        # label1b.config(font=FONT15)
        # my_canvas.create_window(950, 75, window=label1b)
        #
        # label2 = tk.Label(my_window, text='Entrance: i, Exit: O')
        # label2.config(font=FONT15)
        # my_canvas.create_window(950, 100, window=label2)
        #
        # label2a = tk.Label(my_window, text="Pillars: A, E, I, P")
        # label2a.config(font=FONT15)
        # my_canvas.create_window(950, 125, window=label2a)
        #
        # label3 = tk.Label(my_window, text='North/South Doors: Green')
        # label3.config(font=FONT15)
        # my_canvas.create_window(950, 150, window=label3)
        #
        # label4 = tk.Label(my_window, text='East/West Doors: Blue')
        # label4.config(font=FONT15)
        # my_canvas.create_window(950, 175, window=label4)
        #
        # label5 = tk.Label(my_window, text='No Door => Closed Wall')
        # label5.config(font=FONT15)
        # my_canvas.create_window(950, 200, window=label5)
        #
        # label6 = tk.Label(my_window, text='Two Adj Doors => Path Exists')
        # label6.config(font=FONT15)
        # my_canvas.create_window(950, 225, window=label6)
        #
        # label6a = tk.Label(my_window, text='Adventurer: Person Image')
        # label6a.config(font=FONT15)
        # my_canvas.create_window(950, 250, window=label6a)
        #
        # label7 = tk.Label(my_window, text='  FINAL SCORE:', fg='blue')
        # label7.config(font=FONT15)
        # my_canvas.create_window(950, 300, window=label7)

        my_window.mainloop()  # enter main loop


if __name__ == "__main__":
    name = "XYZ"

    """
    Enter the column and row count of the maze.
    Currently handles square mazes. So keep both the same.
    """
    row_count = 4
    col_count = 4     # Keep row_count and col_count same
    dungeon_gui = TriviaMazeGUI(int(row_count), int(col_count))
    dungeon_gui.main()


