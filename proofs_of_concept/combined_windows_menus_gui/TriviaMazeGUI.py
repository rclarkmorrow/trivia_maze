from tkinter import *
import tkinter as tk
import random
import pickle
from Adventurer import Adventurer
from Dungeon import Dungeon
from DungeonAdventure import DungeonAdventure
from tkinter import messagebox

from trivia_question_gui import Trivia

FONT15 = ('Arial', 15)
FONT32 = ('Arial', 32)

BGB = 'black'
BGY = 'yellow'
BGW = 'white'
FGG = 'green'
FGY = 'yellow'
FGB = 'black'
FGBL = 'blue'

class DungeonGui(object):

    def __init__(self,num_rows, num_cols):
        """
        Initialization of the variables
        """
        global n_rows, n_cols, row_blank_space, col_blank_space, adventurer, hit_point, pillar_collected, \
            healing_potion_count, vision_potion_count, \
            north_doors_list, south_doors_list, east_doors_list, west_doors_list, \
            content_list, content_indices_list, \
            adventurer_i_index, adventurer_j_index, \
            curr_i, curr_j, my_image

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
        adventurer = Adventurer(" ")
        hit_point = adventurer.hit_points
        pillar_collected = adventurer.pillar_collected
        healing_potion_count = adventurer.healing_potion_count
        vision_potion_count = adventurer.vision_potion_count

        """
        Box indicating the current adventurer location
        """
        self.x1 = 150
        self.y1 = 40
        self.x2 = 350
        self.y2 = 240

        """
        For Pickling
        """
        north_doors_list = [[]]
        south_doors_list = [[]]
        east_doors_list = [[]]
        west_doors_list = [[]]
        content_list = [[]]


    def create_tk_windows(self):
        """
        Creates tk windows and canvas
        """
        global my_window, my_canvas, adventurer_image, window_width, window_height, my_canvas2, my_canvas3
        """
        Creating a window and canvas
        """
        my_window = tk.Tk()
        my_window.title('WELCOME TO THE TRIVIA MAZE')
        window_width = 1100
        window_height = 1100
        my_canvas = tk.Canvas(master=my_window, width=window_height, height=window_height, background=BGB)
        adventurer_image = PhotoImage(master=my_canvas, file="adventurer2_img.png")

        # Creating Frames
        main_frame = LabelFrame(my_window, text='Main Frame', padx=10, pady=10)
        main_frame.pack(side = LEFT, anchor=N, expand=YES, fill=BOTH)

        move_frame = LabelFrame(my_window, text='Move Frame', padx=2, pady=2)
        move_frame.pack(side = TOP, anchor = E, expand=YES, fill=BOTH)

        # trivia_frame = LabelFrame(my_window, text='Trivia Frame', padx=10, pady=10)
        # trivia_frame.pack(side = BOTTOM, anchor=E, expand=YES, fill=BOTH)

        # Create Canvas
        my_canvas = tk.Canvas(main_frame, width=800, height=500, background=BGB)
        my_canvas2 = tk.Canvas(move_frame, width=500, height=275, background=BGB)
        #my_canvas3 = tk.Canvas(trivia_frame, width=500, height=900, background=BGB)

        # Create Box
        my_canvas2.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=BGB, outline='white')

        # Create a Box to indicate the position of the adventurer
        my_canvas2.create_text(self.x1, self.y1 + 30, text="You are currently in \n Room",
                               font=("Helvetica", 14), fill='red', anchor='w')



        """
        Binding the key board strokes with GUI
        """
        my_window.bind("<Left>", DungeonGui.left)
        my_window.bind("<Right>", DungeonGui.right)
        my_window.bind("<Up>", DungeonGui.up)
        my_window.bind("<Down>", DungeonGui.down)

        """
        File Menu
        """
        DungeonGui.create_menus(self)

    def current_location(self):
        # Create Box
        my_canvas2.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="black", outline='white')

        # Create a Box to indicate the position of the adventurer
        my_canvas2.create_text(self.x1, self.y1 + 30, text="You are currently in \n Room",
                                    font=("Helvetica", 14), fill='red', anchor='w')

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
                                           (i+1) * self.row_height,fill="yellow")
            my_canvas.pack()
            my_canvas.update()

    def create_content(self, i, j, content):
        """
        Create content such as Pillar, Pit etc at a specified Index of the room.
        """
        if content == 'A' or content == 'E' or content == 'E' or content == 'P' or content == 'I':
            my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                                  i * self.row_height + row_blank_space + self.row_height / 3,
                                  text=content,
                                  font=FONT15,
                                  fill=FGBL)
            content_list.append((i,j, content))

        else:
            my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                                  i * self.row_height + row_blank_space + self.row_height / 3,
                                  text=content,
                                  font=FONT15,
                                  fill=FGBL)
            content_list.append((i,j,content))

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
            north_doors_list.append((i,j))
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
            south_doors_list.append((i,j))
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
            east_doors_list.append((i, j))
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
            west_doors_list.append((i,j))
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
            adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion, my_image

        # Display Current location
        x1, y1, x2, y2 = 150, 40, 350, 240
        my_canvas2.create_rectangle(x1, y1, x2, y2, fill="black", outline='white')
        my_canvas2.create_text(x1, y1 + 30, text="You are currently in \n Room",
                                font=("Helvetica", 14), fill='red', anchor='w')

        # Indices of current location of the adventurer
        curr_i = adventurer_i_index
        curr_j = adventurer_j_index
        next_i = adventurer_i_index

        if event.keysym=='Left':
            adventurer_j_index = adventurer_j_index-1
            next_j=adventurer_j_index
            DungeonGui.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if DungeonAdventure.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
            x = -100 # Keep this same as 'self.col_width'
            y = 0
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_j_index = adventurer_j_index + 1  # This takes care of repeated key press

        # Display Current location
        content = "(" + str(adventurer_i_index) + "," + str(adventurer_j_index) + ")"
        my_canvas2.create_text(250, 150, text=content, font=("Helvetica", 40), fill='Red', tag="location")

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!",fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 3500, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!",fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(adventurer.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950,400, window=label_hit_points)

            return

    def right(event):
        """
        Event Handling Method for RIGHT key stroke movements
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols,\
            adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        # Display Current location
        x1, y1, x2, y2 = 150, 40, 350, 240
        my_canvas2.create_rectangle(x1, y1, x2, y2, fill="black", outline='white')
        my_canvas2.create_text(x1, y1 + 30, text="You are currently in \n Room",
                                font=("Helvetica", 14), fill='red', anchor='w')

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index
        next_i = adventurer_i_index

        if event.keysym == 'Right':
            adventurer_j_index = adventurer_j_index + 1
            next_j = adventurer_j_index
            DungeonGui.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if DungeonAdventure.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
            x = 100
            y = 0
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_j_index = adventurer_j_index - 1

        content = "(" + str(adventurer_i_index) + "," + str(adventurer_j_index) + ")"
        my_canvas2.create_text(250, 150, text=content, font=("Helvetica", 40), fill='Red')


        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(adventurer.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            return

    def up(event):
        """
        Event Handling Method to create UP key stroke movements
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols, \
            adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        # Display Current location
        x1, y1, x2, y2 = 150, 40, 350, 240
        my_canvas2.create_rectangle(x1, y1, x2, y2, fill="black", outline='white')
        my_canvas2.create_text(x1, y1 + 30, text="You are currently in \n Room",
                                font=("Helvetica", 14), fill='red', anchor='w')

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index

        next_j = adventurer_j_index
        if event.keysym == 'Up':
            adventurer_i_index = adventurer_i_index-1
            next_i = adventurer_i_index
            DungeonGui.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if DungeonAdventure.if_passable(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols):
            x = 0
            y = -100  # Keep this same as self.row_height
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_i_index = adventurer_i_index + 1

         # Display Current location
        content = "(" + str(adventurer_i_index) + "," + str(adventurer_j_index) + ")"
        my_canvas2.create_text(250, 150, text=content, font=("Helvetica", 40), fill='Red', tag="location")

        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=('Arial', 15))
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(adventurer.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)

            return

    def down(event):
        """
        Event Handling Method to create DOWN keystroke movement
        """
        global adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, \
            adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

        # Display Current location
        x1, y1, x2, y2 = 150, 40, 350, 240
        my_canvas2.create_rectangle(x1, y1, x2, y2, fill="black", outline='white')
        my_canvas2.create_text(x1, y1 + 30, text="You are currently in \n Room",
                                font=("Helvetica", 14), fill='red', anchor='w')

        curr_i = adventurer_i_index
        curr_j = adventurer_j_index

        next_j = adventurer_j_index
        if event.keysym == 'Down':
            adventurer_i_index = adventurer_i_index+1
            next_i = adventurer_i_index
            DungeonGui.score_card(dng, curr_i, curr_j, next_i, next_j, n_rows, n_cols)

        if DungeonAdventure.if_passable(dng,curr_i,curr_j,next_i,next_j,n_rows, n_cols):
            x = 0
            y = 100
            my_canvas.move(my_image, x, y)
        else:
            x = 0
            y = 0
            my_canvas.move(my_image, x, y)
            adventurer_i_index = adventurer_i_index - 1

        # Display Current location
        content = "(" + str(adventurer_i_index) + "," + str(adventurer_j_index) + ")"
        my_canvas2.create_text(250, 150, text=content, font=("Helvetica", 40), fill='Red', tag="location")


        if (next_i, next_j) == (exit_i_index, exit_j_index):
            label_congrats = tk.Label(my_window, text="Congratulations!", fg=FGG)
            label_congrats.config(font=FONT15)
            my_canvas.create_window(950, 350, window=label_congrats)

            label_dest = tk.Label(my_window, text="Reached Destination!", fg=FGG)
            label_dest.config(font=FONT15)
            my_canvas.create_window(950, 375, window=label_dest)

            label_hit_points = tk.Label(my_window, text="Total Hit Points: " + str(adventurer.hit_points))
            label_hit_points.config(font=FONT15)
            my_canvas.create_window(950, 400, window=label_hit_points)
            return

    def score_card(dungeon, curr_x, curr_y, next_x, next_y, column_count, row_count):
        """
        Generates score card such as hit points, pillars collected
        """
        global adventurer, hit_point, pillar_collected, healing_potion_count, vision_potion_count, healing_potion,\
            vision_potion

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

    """
    Menus
    """

    def create_menus(self):
        # Create a menu configuration
        my_menu = Menu(my_window)
        my_window.config(menu=my_menu)

        # Create a 'File' menu buttom
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='File', menu=file_menu)

        # Create a 'Save Game' button
        file_menu.add_command(label='Save Game', command=self.save_game)
        file_menu.add_separator()

        # Create a 'Load Game' button
        file_menu.add_command(label='Load Game', command=self.load_game)
        file_menu.add_separator()

        # Create a 'Exit' button
        file_menu.add_command(label='Exit', command=my_window.quit)
        file_menu.add_separator()

        # Create a 'Help' button
        help_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='Help', menu=help_menu)

        # Create a 'About' button
        help_menu.add_command(label='About', command=self.about_us)
        help_menu.add_separator()

        # Create a 'Game Instructions' button
        help_menu.add_command(label='Game Instructions', command=self.game_instructions)
        help_menu.add_separator()


    def save_game(self):

        """
        The method is to save the game
        When the save game button is pressed this code needs to be executed
        """
        global adventure_i_index, adventurer_j_index, exit_i_index, exit_j_index, my_list_N, \
            curr_i, curr_j, next_i, next_j, n_rows, n_cols

        adventurer_location = [adventurer_i_index, adventurer_j_index, dng]

        filename="output_file_1"
        output_file_1 = open(filename, 'wb')
        pickle.dump(north_doors_list, output_file_1)
        pickle.dump(south_doors_list, output_file_1)
        pickle.dump(east_doors_list, output_file_1)
        pickle.dump(west_doors_list, output_file_1)
        pickle.dump(content_list, output_file_1)
        pickle.dump(adventurer_location, output_file_1)
        my_canvas.delete("all")
        my_canvas2.delete("all")

    def load_game(self):
        """
        This method is used to load the game.

        """
        global my_image

        filename = "output_file_1"
        input_file = open(filename, 'rb')
        north_doors_list = pickle.load(input_file)
        south_doors_list = pickle.load(input_file)
        east_doors_list = pickle.load(input_file)
        west_doors_list = pickle.load(input_file)
        content_list = pickle.load(input_file)
        adventurer_location = pickle.load(input_file)

        for row in north_doors_list:
            for col in row:
                i = int(row[0])
                j = int(row[1])
                my_canvas.create_rectangle(j * self.col_width + 50, i * self.row_height + 20,
                                           j * self.col_width + 80, i * self.row_height + 30,
                                           fill=FGG)
                my_canvas.pack()
                my_canvas.update()

        for row in south_doors_list:
            for col in row:
                i = int(row[0])
                j= int(row[1])
                my_canvas.create_rectangle(j * self.col_width + 50, i * self.row_height + 110,
                                           j * self.col_width + 80, i * self.row_height + 100,
                                           fill=FGG)
                my_canvas.pack()
                my_canvas.update()

        for row in east_doors_list:
            for col in row:
                i = int(row[0])
                j= int(row[1])
                my_canvas.create_rectangle(j * self.col_width + 10 + self.col_width, i * self.row_height + 80,
                                           (j + 1) * self.col_width, (i + 1) * self.row_height - self.row_height / 2,
                                           fill=FGG)
                my_canvas.pack()
                my_canvas.update()

        for row in west_doors_list:
            for col in row:
                i = int(row[0])
                j= int(row[1])
                my_canvas.create_rectangle(j * self.col_width + 20, i * self.row_height + 50,
                                           j * self.col_width + 30, i * self.row_height + 80,
                                           fill=FGG)
                my_canvas.pack()
                my_canvas.update()

        dungeon_gui.create_rooms()

        for row in content_list:
            for col in row:
                i = int(row[0])
                j= int(row[1])
                content = row[2]
                my_canvas.create_text(j * self.col_width + col_blank_space + self.col_width / 3,
                                      i * self.row_height + row_blank_space + self.row_height / 3,
                                      text=content, font=FONT15, fill=FGBL)
                my_canvas.pack()
                my_canvas.update()

        adventurer_i_index=adventurer_location[0]
        adventurer_j_index = adventurer_location[1]
        dng=adventurer_location[2]
        my_image=dungeon_gui.create_adventurer(adventurer_j_index * 100 + 32, adventurer_i_index * 100 + 32)

        # Display Current location
        x1, y1, x2, y2 = 150, 40, 350, 240
        my_canvas2.create_rectangle(x1, y1, x2, y2, fill="black", outline='white')
        my_canvas2.create_text(x1, y1 + 30, text="You are currently in \n Room",\
                               font=FONT15, fill='red', anchor='w')
        content = "(" + str(adventurer_i_index) + "," + str(adventurer_j_index) + ")"
        my_canvas2.create_text(250, 150, text=content, font=FONT32, fill='Red')
        my_canvas.pack()
        my_canvas.update()

    def about_us(self):
        """
        This methods displays the 'about us' content
        """
        messagebox.showinfo('About Us', 'This is a Trivia maze game')

    def game_instructions(self):
        """
        This method displays the game instructions
        """
        messagebox.showinfo('Instructions', 'Step 1: Read the Trivia Questions\n'
                                            'Step 2: Select and Submit the answer\n'
                                            'Step 3: Use the arrows to traverse\n'
                                            'Step 4: Move from entrance to exit')

    def main(self):
        """
        This is the main method and Entry point for the program.
        """
        global my_image, adventurer_i_index, adventurer_j_index, dng, exit_i_index, exit_j_index, n_rows, n_cols
        adventurer_i_index = 0
        adventurer_j_index = 0

        # Create tk windows and bind key strokes
        DungeonGui.create_tk_windows(self)

        # Create GUI rooms
        dungeon = DungeonGui(n_rows, n_cols)
        dungeon.create_rooms()

        # Populate the GUI rooms with dungeon content
        dng = Dungeon(n_rows, n_cols)
        dng.dungeon_generator()
        print(dng)
        for i in range(0, n_rows):
            for j in range(0, n_cols):
                row_index = i
                col_index = j
                content = dng.room_list[i][j].room_content
                dungeon.create_content(row_index, col_index, content)

                east_door_symbol = dng.room_list[i][j].room_matrix[1][2]
                dungeon.create_east_door(row_index, col_index, east_door_symbol)

                west_door_symbol = dng.room_list[i][j].room_matrix[1][0]
                dungeon.create_west_door(row_index, col_index, west_door_symbol)

                north_door_symbol = dng.room_list[i][j].room_matrix[0][1]
                dungeon.create_north_door(row_index, col_index, north_door_symbol)

                south_door_symbol = dng.room_list[i][j].room_matrix[2][1]
                dungeon.create_south_door(row_index, col_index, south_door_symbol)

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
        # label1a = tk.Label(my_window, text='INSTRUCTIONS:',fg="blue")
        # label1a.config(font=('Arial', 15))
        # my_canvas.create_window(950, 50, window=label1a)

        Trivia(my_window)
        my_canvas2.pack()
        my_canvas2.update()
        my_window.mainloop()  # main loop


if __name__ == "__main__":
    name = "XYZ"

    """
    Enter the column and row count of the maze.
    Currently handles square mazes. So keep both the same.
    """
    row_count = 4
    col_count = 4     # Keep row_count and col_count same
    dungeon_gui = DungeonGui(int(row_count), int(col_count))
    dungeon_gui.main()
