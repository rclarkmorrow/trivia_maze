
from tkinter import *
import tkinter as tk
import random
from Adventurer import Adventurer
from Dungeon import Dungeon
from DungeonAdventure import DungeonAdventure

FONT15 = ('Arial', 15)
FONT32 = ('Arial', 32)

BGB = 'black'
BGY = 'yellow'
BGW = 'white'
FGG = 'green'
FGY = 'yellow'
FGB = 'black'
FGBL = 'blue'


class TriviaMaze(object):

    def __init__(self, num_rows, num_cols):

        """
        Initializing Number of Rows and Columns of the Dungeon maze
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        self.__n_rows = num_rows
        self.__n_cols = num_cols

        """
        Initializing spacing between rooms
        """
        self.__row_blank_space = 30
        self.__col_blank_space = 30
        """
        Initializing the room sizes
        """
        self.__col_width = 100
        self.__row_height = 100

        """
        Score Card Initialisation
        """
        self.__adventurer = Adventurer(" ")
        self.__hit_point = self.__adventurer.hit_points
        self.__pillar_collected = self.__adventurer.pillar_collected
        self.__healing_potion_count = self.__adventurer.healing_potion_count
        self.__vision_potion_count = self.__adventurer.vision_potion_count

        """
        Create tk windows
        """
        self.__my_window = tk.Tk()
        self.__my_window.title('WELCOME TO THE TRIVIA MAZE GAME')
        self.__window_width = 1100
        self.__window_height = 1100

        self.__adventurer_i_index = 0
        self.__adventurer_j_index = 0

    def create_tk_windows(self):

        my_canvas = tk.Canvas(master=self.__my_window,
                              width=self.__window_height,
                              height=self.__window_height,
                              background=BGB)
        adventurer_image = PhotoImage(master=my_canvas, file="adventurer2_img.png")
        """
        Binding the key board strokes with GUI
        """
        # self.__my_window.bind("<Left>", TriviaMaze.left)
        # self.__my_window.bind("<Right>", TriviaMaze.right)
        # self.__my_window.bind("<Up>", TriviaMaze.up)
        # self.__my_window.bind("<Down>", TriviaMaze.down)

        def create_rooms():
            """
            The method creates rooms on canvas
            """
            for i in range(0, self.__num_rows):
                for j in range(0, self.__num_rows):
                    my_canvas.create_rectangle(j * self.__col_width + self.__col_blank_space,
                                               i * self.__row_height + self.__row_blank_space,
                                               (j+1) * self.__col_width,
                                               (i+1) * self.__row_height,
                                               fill=BGY)
                my_canvas.pack()
                my_canvas.update()

        def create_content(i, j, content):
            """
            Create content such as Pillar, Pit etc at a specified Index of the room.
            """
            if content == 'A' or content == 'E' or content == 'E' or content == 'P' or content == 'I':
                my_canvas.create_text(j * self.__col_width + self.__col_blank_space + self.__col_width / 3,
                                      i * self.__row_height + self.__row_blank_space + self.__row_height / 3,
                                      text=content, font=FONT15, fill=FGBL)
            else:
                my_canvas.create_text(j * self.__col_width + self.__col_blank_space + self.__col_width / 3,
                                      i * self.__row_height + self.__row_blank_space + self.__row_height / 3,
                                      text=content, font=FONT15, fill=FGBL)

        def create_north_door(i, j, north_door_symbol):
            """
            Creates north door for a room
            """
            if north_door_symbol == '-':
                my_canvas.create_rectangle(j*self.__col_width+50, i*self.__row_height+20,
                                           j*self.__col_width+80, i*self.__row_height+30,
                                           fill="green")
                my_canvas.pack()
                my_canvas.update()

        def create_south_door(i, j, south_door_symbol):
            """
            Creates south door for a room
            """
            if south_door_symbol == '-':
                my_canvas.create_rectangle(j*self.__col_width+50,
                                           i*self.__row_height+110,
                                           j*self.__col_width+80,
                                           i*self.__row_height+100,
                                           fill="green")
                my_canvas.pack()
                my_canvas.update()

        def create_east_door(i, j, east_door_symbol):
            """
            Creates east door for a room
            """
            if east_door_symbol == '|':
                my_canvas.create_rectangle(j*self.__col_width+10+self.__col_width,
                                           i*self.__row_height+80,
                                           (j+1)*self.__col_width,
                                           (i+1)*self.__row_height-self.__row_height/2,
                                           fill="green")
            my_canvas.pack()
            my_canvas.update()

        def create_west_door(i, j, west_door_symbol):
            """
            Creates west door for a room
            """
            if west_door_symbol == '|':
                my_canvas.create_rectangle(j*self.__col_width+20, i*self.__row_height+50,
                                           j*self.__col_width+30, i*self.__row_height+80,
                                           fill="green")
            my_canvas.pack()
            my_canvas.update()

        def create_adventurer(i, j):
            """
            Creates adventurers on canvas
            """
            return my_canvas.create_image(i, j, anchor=NW, image=adventurer_image)

        def left(event):
            """
            Event Handling Method for LEFT keystroke movements
            """
            # global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols,\
            #     adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            #     vision_potion

            curr_i = self.__adventurer_i_index
            curr_j = self.__adventurer_j_index
            next_i = self.__adventurer_i_index

            if event.keysym == 'Left':
                adventurer_j_index = self.__adventurer_j_index-1
                next_j = adventurer_j_index
                score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

            if DungeonAdventure.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
                x = -100  # Keep this same as 'self.col_width'
                y = 0
                my_canvas.move(my_image, x, y)
            else:
                x = 0
                y = 0
                my_canvas.move(my_image, x, y)
                adventurer_j_index = self.__adventurer_j_index + 1  # This takes care of repeated key press

            if (next_i, next_j) == (exit_i_index, exit_j_index):
                label_congrats = tk.Label(self.__my_window, text="Congratulations!", fg='green')
                label_congrats.config(font=FONT15)
                my_canvas.create_window(950, 3500, window=label_congrats)

                label_dest = tk.Label(self.__my_window, text="Reached Destination!", fg='green')
                label_dest.config(font=FONT15)
                my_canvas.create_window(950, 375, window=label_dest)

                label_hit_points = tk.Label(self.__my_window, text="Total Hit Points: " + str(adventurer.hit_points))
                label_hit_points.config(font=FONT15)
                my_canvas.create_window(950, 400, window=label_hit_points)

                label_pillars = tk.Label(self.__my_window, text="Pillars Collected: " + str(adventurer.pillar_collected))
                label_pillars.config(font=FONT15)
                my_canvas.create_window(950, 425, window=label_pillars)
                return

        def right(event):
            """
            Event Handling Method for RIGHT key stroke movements
            """
            # global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols,\
            #     adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            #     vision_potion

            curr_i = self.__adventurer_i_index
            curr_j = self.__adventurer_j_index
            next_i = self.__adventurer_i_index

            if event.keysym == 'Right':
                adventurer_j_index = self.__adventurer_j_index + 1
                next_j = adventurer_j_index
                score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

            if DungeonAdventure.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
                x = 100
                y = 0
                my_canvas.move(my_image, x, y)
            else:
                x = 0
                y = 0
                my_canvas.move(my_image, x, y)
                adventurer_j_index = self.__adventurer_j_index - 1

            if (next_i, next_j) == (exit_i_index, exit_j_index):
                label_congrats = tk.Label(self.__my_window, text="Congratulations!", fg='green')
                label_congrats.config(font=FONT15)
                my_canvas.create_window(950, 350, window=label_congrats)

                label_dest = tk.Label(self.__my_window, text="Reached Destination!", fg='green')
                label_dest.config(font=FONT15)
                my_canvas.create_window(950, 375, window=label_dest)

                label_hit_points = tk.Label(self.__my_window, text="Total Hit Points: " + str(adventurer.hit_points))
                label_hit_points.config(font=FONT15)
                my_canvas.create_window(950, 400, window=label_hit_points)

                label_pillars = tk.Label(self.__my_window, text="Pillars Collected: " + str(adventurer.pillar_collected))
                label_pillars.config(font=FONT15)
                my_canvas.create_window(950, 425, window=label_pillars)
                return

        def up(event):
            """
            Event Handling Method to create UP key stroke movements
            """
            # global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols, \
            #     adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            #     vision_potion

            curr_i = self.__adventurer_i_index
            curr_j = self.__adventurer_j_index

            next_j = self.__adventurer_j_index
            if event.keysym == 'Up':
                adventurer_i_index = self.__adventurer_i_index-1
                next_i = adventurer_i_index
                score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

            if DungeonAdventure.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
                x = 0
                y = -100  # Keep this same as self.row_height
                my_canvas.move(my_image, x, y)
            else:
                x = 0
                y = 0
                my_canvas.move(my_image, x, y)
                adventurer_i_index = self.__adventurer_i_index + 1

            if (next_i, next_j) == (exit_i_index, exit_j_index):
                label_congrats = tk.Label(self.__my_window, text="Congratulations!", fg='green')
                label_congrats.config(font=FONT15)
                my_canvas.create_window(950, 350, window=label_congrats)

                label_dest = tk.Label(self.__my_window, text="Reached Destination!", fg='green')
                label_dest.config(font=FONT15)
                my_canvas.create_window(950, 375, window=label_dest)

                label_hit_points = tk.Label(self.__my_window, text="Total Hit Points: " + str(adventurer.hit_points))
                label_hit_points.config(font=FONT15)
                my_canvas.create_window(950, 400, window=label_hit_points)

                label_pillars = tk.Label(self.__my_window, text="Pillars Collected: " + str(adventurer.pillar_collected))
                label_pillars.config(font=FONT15)
                my_canvas.create_window(950, 425, window=label_pillars)
                return

        def down(event):
            """
            Event Handling Method to create DOWN keystroke movement
            """
            # global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, \
            #     adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            #     vision_potion

            curr_i = self.__adventurer_i_index
            curr_j = self.__adventurer_j_index

            next_j = self.__adventurer_j_index
            if event.keysym == 'Down':
                adventurer_i_index = self.__adventurer_i_index+1
                next_i = adventurer_i_index
                score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

            if DungeonAdventure.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
                x = 0
                y = 100
                my_canvas.move(my_image, x, y)
            else:
                x = 0
                y = 0
                my_canvas.move(my_image, x, y)
                adventurer_i_index = self.__adventurer_i_index - 1

            if (next_i, next_j) == (exit_i_index, exit_j_index):
                label_congrats = tk.Label(self.__my_window, text="Congratulations!", fg='green')
                label_congrats.config(font=FONT15)
                my_canvas.create_window(950, 350, window=label_congrats)

                label_dest = tk.Label(self.__my_window, text="Reached Destination!", fg='green')
                label_dest.config(font=FONT15)
                my_canvas.create_window(950, 375, window=label_dest)

                label_hit_points = tk.Label(self.__my_window, text="Total Hit Points: " + str(adventurer.hit_points))
                label_hit_points.config(font=FONT15)
                my_canvas.create_window(950, 400, window=label_hit_points)

                label_pillars = tk.Label(self.__my_window, text="Pillars Collected: " + str(adventurer.pillar_collected))
                label_pillars.config(font=FONT15)
                my_canvas.create_window(950, 425, window=label_pillars)
                return

        def score_card(dungeon, curr_x, curr_y, next_x, next_y, column_count, row_count):
            """
            Generates score card such as hit points, pillars collected
            """
            # global adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            #     vision_potion

            if DungeonAdventure.if_passable(dungeon, curr_x, curr_y, next_x, next_y, column_count, row_count):
                next_room = dungeon.room_list[next_x][next_y]
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
                adventurer.hit_points = hit_point
                return

    # Create tk windows and bind key strokes
    create_tk_windows()


    # Populate the GUI rooms with dungeon content
    dng = Dungeon(n_rows, n_cols)
    dng.dungeon_generator()
    print(dng)
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            row_index = i
            col_index = j
            content = dng.room_list[i][j].room_content
            dng.create_content(row_index, col_index, content)

            # east_door_symbol = dng.room_list[i][j].room_matrix[1][2]
            dungeon.create_east_door(row_index, col_index, '|')

            # west_door_symbol = dng.room_list[i][j].room_matrix[1][0]
            dungeon.create_west_door(row_index, col_index, '|')

            # north_door_symbol = dng.room_list[i][j].room_matrix[0][1]
            dungeon.create_north_door(row_index, col_index, '-')

            # south_door_symbol = dng.room_list[i][j].room_matrix[2][1]
            dungeon.create_south_door(row_index, col_index, '-')

            if content == 'i':
                adventurer_i_index = i
                adventurer_j_index = j
                my_image = dungeon.create_adventurer(adventurer_j_index*100+32,
                                                     adventurer_i_index*100+32)

            if content == 'O':
                exit_i_index = i
                exit_j_index = j

        """
         Displays
        """
        label1a = tk.Label(self.__my_window, text='INSTRUCTIONS:',fg="blue")
        label1a.config(font=FONT15)
        my_canvas.create_window(950, 50, window=label1a)

        label1b = tk.Label(self.__my_window, text='Use Keyboard Arrow Keys')
        label1b.config(font=FONT15)
        my_canvas.create_window(950, 75, window=label1b)

        label2 = tk.Label(self.__my_window, text='Entrance: i, Exit: O')
        label2.config(font=FONT15)
        my_canvas.create_window(950, 100, window=label2)

        label2a = tk.Label(self.__my_window, text="Pillars: A, E, I, P")
        label2a.config(font=FONT15)
        my_canvas.create_window(950, 125, window=label2a)

        label3 = tk.Label(self.__my_window, text='North/South Doors: Green')
        label3.config(font=FONT15)
        my_canvas.create_window(950, 150, window=label3)

        label4 = tk.Label(self.__my_window, text='East/West Doors: Blue')
        label4.config(font=FONT15)
        my_canvas.create_window(950, 175, window=label4)

        label5 = tk.Label(self.__my_window, text='No Door => Closed Wall')
        label5.config(font=FONT15)
        my_canvas.create_window(950, 200, window=label5)

        label6 = tk.Label(self.__my_window, text='Two Adj Doors => Path Exists')
        label6.config(font=FONT15)
        my_canvas.create_window(950, 225, window=label6)

        label6a = tk.Label(self.__my_window, text='Adventurer: Person Image')
        label6a.config(font=FONT15)
        my_canvas.create_window(950, 250, window=label6a)

        label7 = tk.Label(self.__my_window, text='  FINAL SCORE:', fg='blue')
        label7.config(font=FONT15)
        self.__my_canvas.create_window(950, 300, window=label7)

        self.__my_window.mainloop()  # enter main loop


if __name__ == "__main__":
    name = "XYZ"

    """
    Enter the column and row count of the maze.
    Currently handles square mazes. So keep both the same.
    """
    row_count = 4
    col_count = 4     # Keep row_count and col_count same
    dungeon_gui = TriviaMaze(int(row_count), int(col_count))
    dungeon_gui.main()
