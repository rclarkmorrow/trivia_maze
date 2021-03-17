import tkinter as tk
from tkinter import messagebox
import pickle
from playsound import playsound
from trivia_game_interface import TriviaGameInterface

FONT = ('Arial', 14)
H_FONT = ('Arial', 18)
BGB = 'black'
BGY = 'yellow'
FGG = 'green'
FGY = 'yellow'
BGW = 'white'
FGB = 'black'


class QuestionView(tk.Frame):
    """
    This class is used to display the Trivia QuestionView at the bottom
    right quadrant.
    """
    def __init__(self, master=None):
        """"
        This method initializes the gui frames, question view grid, radio
        buttons and submit buttons
        """
        tk.Frame.__init__(self, master=master)
        self.config(bg=BGB)
        self.radio_buttons = []
        self.radio_selection = tk.StringVar()
        self.user_answer = None
        self.columnconfigure(0, weight=1)
        # Set up QuestionView grid.
        for row in range(9):
            self.rowconfigure(row, weight=1)
        # Add View title.
        self.question_view_title = tk.Label(
            self,
            justify=tk.CENTER,
            font=H_FONT,
            text='QUESTION',
            wraplength=220,
            fg=FGY,
            bg=BGB)
        self.question_view_title.grid(row=0, column=0, rowspan=2, sticky='nsew')
        self.submit = tk.Button(
            self,
            text='Submit',
            font=FONT,
            bg=BGY,
            fg=BGB,
            wraplength=220,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.submit.grid(row=8, column=0, rowspan=2, sticky='e')
        self.load_question(update=False)

    @property
    def __inactive_question(self):
        """
        This method is used to display the start the game button.
        It is posed as an inactive question so that it can work with
        the existing database questions
        """

        return {
            'Question': 'To play the game, click the "Start the game" button below.',
            'Answers': {
                # 'a': '',
                # 'b': '',
                # 'c': '',
            },
            # 'Correct': ['c']
        }

    def on_change(self):
        """
            This method retrieves the user selected radio button,
            and assigns its value to the view's user answer.
        """
        self.user_answer = [self.radio_selection.get()]
        print(f'Answer on change: {self.user_answer}')

    def load_question(self, question=None, update=True):
        """ Loads a new question, or the inactive placeholder """

        if not question:
            self.question = self.__inactive_question
            self.submit['text'] = 'Start the game'
            self.submit.update()
        else:
            self.question = question
            self.submit['text'] = 'Submit'
            self.submit.update()
        
        self.question_text = tk.Label(
            self,
            justify=tk.LEFT,
            wraplength=220,
            text=self.question['Question'],
            fg=FGY,
            bg=BGB,
            font='Arial 16 italic'
        )
        self.question_text.update()

        self.question_text.grid(row=3, column=0, pady=(20, 10))
        self.radio_selection.set('z')
        count = 0
        for key, value in self.question['Answers'].items():
            button = tk.Radiobutton(
                self,
                text=value,
                variable=self.radio_selection,
                value=key,
                indicatoron=True,
                font=FONT,
                fg=FGY,
                bg=BGB,
                command=self.on_change
            )
            button.deselect()
            button.grid(row=count + 4, column=0, sticky='w')
            self.radio_buttons.append(button)
            count += 1

    def reset_question(self):
        """
        Resets the question by destroying the question and answer texts.
        """
        self.question_text.destroy()
        for answer in self.radio_buttons:
            answer.destroy()


class MazeView(tk.Frame):
    """
    This is used to display the Maze view on the top left quadrant of
    the screen.
    """
    def __init__(self, master=None, rows=4, columns=4, 
                 player_position=None, exit_position=None):
        """
        Initialization of the maze view gui frame, rooms, player positions,
        player images, and exit positions
        """
        tk.Frame.__init__(self, master=master)
        self.rooms = {}
        self.player_position = player_position
        self.exit_position = exit_position
        self.player_image = tk.PhotoImage(file="Player.PNG")
        self.exit_image = tk.PhotoImage(file="ExitDoor.png")
        for row in range(rows):
            self.rowconfigure(row, weight=1, minsize=80)
            for column in range(columns):
                door_right = None
                door_down = None
                self.columnconfigure(column, weight=1, minsize=80)
                room = tk.Frame(self)
                for cell in range(3):
                    room.rowconfigure(cell, weight=1)
                    room.columnconfigure(cell, weight=1)
                room_center = tk.Canvas(room)
                room_center.config(bg=FGY)
                room_center.grid(row=1, column=1, ipadx=10, ipady=10, sticky='nsew')
                if column < columns - 1:
                    door_right = tk.Canvas(room, bg='green', height=40)
                    door_right.grid(row=1, column=2)
                if row < rows -1:
                    door_down = tk.Canvas(room, bg='green', width=40)
                    door_down.grid(row=2, column=1)
                room.grid(row=row, column=column)
                image = room_center.create_image(
                    50,
                    70,
                    image=self.player_image,
                    anchor=tk.SE
                )
                room_center.delete(image)
                self.rooms[row, column] = {
                    'room': room,
                    'room_center': room_center,
                    'door_right': door_right,
                    'door_down': door_down,
                }

        row, col = self.player_position
        self.player = self.rooms[row, col]['room_center'].create_image(
            50,
            70,
            image=self.player_image,
            anchor=tk.SE
        )
        row, col = self.exit_position
        self.exit = self.rooms[row, col]['room_center'].create_image(
            75,
            70,
            image=self.exit_image,
            anchor=tk.SE
        )

    def move_player(self, old_position, new_position, toggle=False):
        """
        This methods moves the player to a new position. The player
        image is moved.
        """
        row, col = old_position
        self.rooms[row, col]['room_center'].delete(self.player)
        row, col = new_position
        self.player = self.rooms[row, col]['room_center'].create_image(
            50,
            70,
            image=self.player_image,
            anchor=tk.SE
        )


class InfoView(tk.Frame):
    """
    This method display info view at the bottom left quadrant of the screen.
    """
    def __init__(self, master=None, text=None):
        tk.Frame.__init__(self, master=master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.label = tk.Label(self, text=text, bg=BGB, fg=FGY)
        self.label.grid(row=0, column=0, sticky='nsew')


class RoomView(tk.Frame):
    """
    This method is used to display room view in the top right quadrant. Here
    the player move buttons are located.
    """
    def __init__(self, master=None, current_room=None):
        """
        Initializes the room view gui frame, grid, move buttons, labels.
        """
        tk.Frame.__init__(self, master=master)
        self.config(bg=BGB)
        self.current_room = current_room
        for cell in range(3):
            self.rowconfigure(cell, weight=1)
            self.columnconfigure(cell, weight=1)
        self.rowconfigure(1, weight=1, minsize=100)
        self.columnconfigure(1, weight=1, minsize=50)

        self.room = tk.Frame(self, height=50, width=50,
                             highlightbackground=FGY,
                             highlightthickness=5)
        self.room.grid(row=1, column=1, sticky='nsew')
        self.room.rowconfigure(0, weight=1)
        self.room.columnconfigure(0, weight=1)
        row, col = self.current_room.position

        self.player_image = tk.PhotoImage(file="PlayerBigImg.png")
        self.room_label = tk.Label(
            self.room,
            image=self.player_image,
            bg=BGB,
            fg=FGY
        )
        self.room_label.grid(row=0, column=0, sticky='nsew')

        self.right = tk.Button(
            self,
            text='Move Right',
            font=FONT,
            bg=BGY,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.right.grid(row=1, column=2, sticky='w')

        self.up = tk.Button(
            self,
            text='Move Up',
            font=FONT,
            bg=BGY,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.up.grid(row=0, column=1, sticky='s')
        self.down = tk.Button(
            self,
            text='Move Down',
            font=FONT,
            bg=BGY,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.down.grid(row=2, column=1, sticky='n')

        self.left = tk.Button(
            self,
            text='Move Left',
            font=FONT,
            bg=BGY,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.left.grid(row=1, column=0, sticky='w')
        self.check_exits()

    def check_exits(self):
        """
        This method checks the exits. Checks for the maze boundaries and
        enables/disables the buttons accordingly.
        """
        if not self.current_room.up:
            print('disable up')
            self.up['state'] = tk.DISABLED
        else:
            print('enable up')
            self.up['state'] = tk.NORMAL
        if not self.current_room.right:
            print('disable right')
            self.right['state'] = tk.DISABLED
        else:
            print('enable right')
            self.right['state'] = tk.NORMAL
        if not self.current_room.down:
            print('disable down')
            self.down['state'] = tk.DISABLED
        else:
            print('enable down')
            self.down['state'] = tk.NORMAL
        if not self.current_room.left:
            print('disable left')
            self.left['state'] = tk.DISABLED
        else:
            print('enable left')
            self.left['state'] = tk.NORMAL

    def update_room(self, current_room=None):
        """
        Updates and displays the current room position.
        """
        if current_room:
            self.current_room = current_room
        row, col = self.current_room.position
        self.room_label.config(text=f'{row}, '
                               f'{col}')
        self.room_label.update()
        self.check_exits()


class TriviaMazeGUI(tk.Tk):
    """
    This is the main class that interfaces/integrates with QuestionView,
    MazeView, InfoView, and RoomView classes.
    """
    def __init__(self):
        """
        Initializes grid layout, labels, and move commands.
        """
        tk.Tk.__init__(self)
        self.game = TriviaGameInterface('Jim', 4, 4)
        self.player_position = self.game.maze_entrance
        self.geometry('900x750')
        self.config(bg=BGB)
        # Create 10 rows and 5 columns
        for row in range(10):
            self.rowconfigure(row, weight=1, minsize=60)
        for col in range(5):
            self.columnconfigure(col, weight=1, minsize=160)
        # Create views and put in grids.
        self.maze_view = MazeView(master=self, rows=4, columns=4,
                                  player_position=self.game.maze_entrance,
                                  exit_position=self.game.maze_exit)
        row, col = self.game.maze_entrance
        room = self.game.game.maze.grid[row][col]
        self.room_view = RoomView(master=self,
                                  current_room=room)

        # ------- Information View ----------------
        self.info_view1 = InfoView(text='INSTRUCTIONS: \n '
                                        'WIN: REACH THE EXIT BY ANSWERING QUESTIONS -- LOOSE: GET 3 WRONG ANSWERS')

        self.info_view1.grid(row=5, column=0, columnspan=3, rowspan=3, sticky='w')

        self.info_view2 = InfoView(text='LIVES REMAINING')
        self.info_view2.grid(row=6, column=0, columnspan=1, rowspan=2, sticky='w')

        self.info_view3 = InfoView(text='3')
        self.info_view3.grid(row=6, column=1, columnspan=1, rowspan=2, sticky='w')

        self.info_view4 = InfoView(text='PLAYER')
        self.info_view4.grid(row=7, column=0, columnspan=1, rowspan=2, sticky='w')
        self.player_image = tk.PhotoImage(file="PlayerMedImg.png")
        self.player_label = tk.Label(master=self,
                                     image=self.player_image)
        self.player_label.grid(row=8, column=1, columnspan=1, rowspan=1, sticky='nw')

        self.info_view6 = InfoView(text='EXIT')
        self.info_view6.grid(row=8, column=0, columnspan=1, rowspan=2, sticky='w')
        self.exit_image = tk.PhotoImage(file="ExitDoor.png")
        self.exit_label = tk.Label(master=self,
                                   image=self.exit_image)
        self.exit_label.grid(row=9, column=1, columnspan=1, rowspan=1, sticky='nw')

        self.question_view = QuestionView(master=self)
        # Grid is 10 x 5, row, column = start position, spans = number of cells to cover.
        self.maze_view.grid(row=0, column=0, rowspan=6, columnspan=3, sticky='nsew')
        self.room_view.grid(row=0, column=3, columnspan=2, rowspan=5, sticky='nsew')

        # --------------- Question View --------------------
        self.question_view.grid(row=5, column=3, columnspan=2, rowspan=5, sticky='n')
        # Add menus.
        self.create_menus()

        self.question_view.submit.config(command=self.is_correct)
        self.room_view.up.config(command=self.move_up)
        self.room_view.right.config(command=self.move_right)
        self.room_view.down.config(command=self.move_down)
        self.room_view.left.config(command=self.move_left)
        self.toggle = False

        self.count_question = 0
        self.count_correct_answer = 0
        self.count_wrong_answer = 0
        self.correct_answer = "NO"
        self.lives_remaining = 3

    def is_correct(self, coord=[3, 2]):
        """
        This method checks if the answer to the trivia question is correct or not.
        """

        self.count_question = self.count_question + 1

        if self.question_view.user_answer:
            if (self.question_view.user_answer ==
                    self.question_view.question['Correct']):
                playsound('applause7.mp3')
                print("CORRECT ANSWER")

                self.correct_answer = "YES"
                self.count_correct_answer = self.count_correct_answer + 1
                self.question_view.submit.config(state='disabled')

            else:
                playsound('boo3.mp3')
                print("WRONG!!")

                self.correct_answer = "NO"
                self.count_wrong_answer = self.count_wrong_answer + 1
                print(self.count_wrong_answer)

                self.lives_remaining = self.lives_remaining - 1
                self.info_view3 = InfoView(text=self.lives_remaining)
                self.info_view3.grid(row=6, column=1, columnspan=1, rowspan=2, sticky='w')

        if self.count_wrong_answer == 3:
            msg_box = messagebox.askquestion("Result", " You LOST.  Would you like "
                                                       "to play another game ?", icon='info')
            if msg_box =='yes':
                TriviaMazeGUI.new_game(self)
            if msg_box == 'no':
                TriviaMazeGUI.exit(self)

            self.count_question = 0
            self.count_correct_answer = 0
            self.count_wrong_answer = 0

        self.question_view.reset_question()
        self.question_view.load_question(question=self.game.get_question())

    def move_up(self):
        """
        This method allows the player to move up
        """

        if self.correct_answer == "NO":
            print("Please Answer the Trivia Question")
            return
        else:
            row, col = self.player_position
            self.maze_view.rooms[row, col]['room_center'].config(bg='red')
            new_row = row - 1
            self.maze_view.move_player([row, col], [new_row, col])
            new_room = self.game.game.maze.grid[new_row][col]
            self.room_view.update_room(new_room)
            self.player_position = [new_row, col]

            self.correct_answer = "NO"
            self.question_view.submit.config(state='normal')

            if self.player_position == self.maze_view.exit_position:
                msg_box = messagebox.askquestion("Result",
                                                 " CONGRATULATIONS ! YOU WON \n "
                                                 "Would you like to play another game ?",
                                                 icon='info')
                if msg_box == 'yes':
                    TriviaMazeGUI.new_game(self)
                if msg_box == 'no':
                    TriviaMazeGUI.exit(self)

    def move_right(self):
        """
        This method allows the player to move right
        """

        if self.correct_answer == "NO":
            print("Please Answer the Trivia Question")
            return
        else:
            row, col = self.player_position
            self.maze_view.rooms[row, col]['room_center'].config(bg='red')
            new_col = col + 1
            self.maze_view.move_player([row, col], [row, new_col])
            new_room = self.game.game.maze.grid[row][new_col]
            self.room_view.update_room(new_room)
            self.player_position = [row, new_col]

            self.correct_answer = "NO"
            self.question_view.submit.config(state='normal')

            if self.player_position == self.maze_view.exit_position:
                msg_box = messagebox.askquestion("Result",
                                                 " CONGRATULATIONS ! YOU WON \n "
                                                 "Would you like to play another game ?",
                                                 icon='info')
                if msg_box == 'yes':
                    TriviaMazeGUI.new_game(self)
                if msg_box == 'no':
                    TriviaMazeGUI.exit(self)

    def move_down(self):
        """
        This method allows the player to move down
        """

        if self.correct_answer == "NO":
            print("Please Answer the Trivia Question")
            return
        else:
            row, col = self.player_position
            self.maze_view.rooms[row, col]['room_center'].config(bg='red')
            new_row = row + 1
            self.maze_view.move_player([row, col], [new_row, col])
            new_room = self.game.game.maze.grid[new_row][col]
            self.room_view.update_room(new_room)
            self.player_position = [new_row, col]

            self.correct_answer = "NO"
            self.question_view.submit.config(state='normal')

            if self.player_position == self.maze_view.exit_position:
                msg_box = messagebox.askquestion("Result",
                                                 " CONGRATULATIONS ! YOU WON \n "
                                                 "Would you like to play another game ?",
                                                 icon='info')
                if msg_box == 'yes':
                    TriviaMazeGUI.new_game(self)
                if msg_box == 'no':
                    TriviaMazeGUI.exit(self)

    def move_left(self):
        """
        This method allows the player to move left
        """

        if self.correct_answer == "NO":
            print("Please Answer the Trivia Question")
            return
        else:
            row, col = self.player_position
            self.maze_view.rooms[row, col]['room_center'].config(bg='red')
            new_col = col - 1
            self.maze_view.move_player([row, col], [row, new_col])
            new_room = self.game.game.maze.grid[row][new_col]
            self.room_view.update_room(new_room)
            self.player_position = [row, new_col]

            self.correct_answer = "NO"
            self.question_view.submit.config(state='normal')

            if self.player_position == self.maze_view.exit_position:
                msg_box = messagebox.askquestion("Result",
                                                 " CONGRATULATIONS ! YOU WON \n "
                                                 "Would you like to play another game ?",
                                                 icon='info')
                if msg_box == 'yes':
                    TriviaMazeGUI.new_game(self)
                if msg_box == 'no':
                    TriviaMazeGUI.exit(self)

    def run(self):
        """
        This is the main entry to the game.
        """
        self.title("TRIVIA MAZE")
        self.mainloop()

    """
    Menus
    """

    def create_menus(self):
        """
        This method creates the File Menu at the top.
        This includes:
        File -> Start New Game, Save Game, Load Game, Exit
        Help->About Us, Instructions
        """
        # Create a menu configuration
        my_menu = tk.Menu(self)
        self.config(menu=my_menu)

        # Create a 'File' menu buttom
        file_menu = tk.Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='File', menu=file_menu)

        # Create a 'Start a New Game' button
        file_menu.add_command(label='Start New Game', command=self.new_game)
        file_menu.add_separator()

        # Create a 'Save Game' button
        file_menu.add_command(label='Save Game', command=self.save_game)
        file_menu.add_separator()

        # Create a 'Load Game' button
        file_menu.add_command(label='Load Game', command=self.load_game)
        file_menu.add_separator()

        # Create a 'Exit' button
        file_menu.add_command(label='Exit', command=self.quit)
        file_menu.add_separator()

        # Create a 'Help' button
        help_menu = tk.Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='Help', menu=help_menu)

        # Create a 'About' button
        help_menu.add_command(label='About', command=self.about_us)
        help_menu.add_separator()

        # Create a 'Game Instructions' button
        help_menu.add_command(label='Game Instructions',
                              command=self.game_instructions)
        help_menu.add_separator()

    def save_game(self):
        """
        The method is to save the game. Pickling/Serialization concept is used.
        """
        filename = "output_file_1"
        output_file_1 = open(filename, 'wb')
        pickle.dump(self.player_position, output_file_1)
        pickle.dump(self.maze_view.exit_position, output_file_1)
        pickle.dump(self.lives_remaining, output_file_1)
        self.maze_view.destroy()
        self.room_view.destroy()
        self.info_view3.destroy()


    def load_game(self):
        """
        This method is used to load the game. Pickling/Serialization concept
        is used.
        """
        filename = "output_file_1"
        input_file = open(filename, 'rb')
        self.player_position = pickle.load(input_file)
        self.maze_view.exit_position = pickle.load(input_file)
        self.lives_remaining = pickle.load(input_file)

        # Create views and put in grids.
        self.maze_view = MazeView(master=self, rows=4, columns=4,
                                  player_position=self.player_position,
                                  exit_position=self.maze_view.exit_position)
        self.maze_view.grid(row=0, column=0, rowspan=6, columnspan=3, sticky='nsew')

        row, col = self.player_position
        room = self.game.game.maze.grid[row][col]
        self.room_view = RoomView(master=self,
                                  current_room=room)
        self.room_view.grid(row=0, column=3, columnspan=2, rowspan=5, sticky='nsew')
        self.room_view.up.config(command=self.move_up)
        self.room_view.right.config(command=self.move_right)
        self.room_view.down.config(command=self.move_down)
        self.room_view.left.config(command=self.move_left)
        self.toggle = False
        self.info_view3 = InfoView(text=self.lives_remaining)
        self.info_view3.grid(row=6, column=1, columnspan=1, rowspan=2, sticky='w')

    def new_game(self):
        """
        This method is used to start a new game
        """
        self.destroy()
        trivia_game = TriviaMazeGUI()
        trivia_game.run()

    def exit(self):
        """
        This method is used to exit the game program.
        """
        self.destroy()

    @staticmethod
    def about_us():
        """
        This methods displays the 'about us' content
        """
        messagebox.showinfo(
            'About Us',
            'Welcome to the Trivia Maze Game.\n\n'
            'This Trivia Maze Game was created by '
            'Raj Birru, Dee Turco and Rick Morrow '
            'as a group project for the University '
            'of Washington Tacoma\'s course TCSS-504.\n\n'
            'TCSS-504 is part of the Graduate '
            'Certificate in Software Development '
            'Engineering program at UW-Tacoma.'
        )

    @staticmethod
    def game_instructions():
        """
        This method displays the 'game instructions'.
        """
        messagebox.showinfo(
            'Instructions',
            'Trivia Maze Game Instructions:\n\n'
            'Your goal is to reach the exit of the maze '
            'by successfully answering questions to gain '
            'entrance to a new room.\n\n'
            'To start, click "Start the game" button\n\n '
            'To move between rooms:\n'
            'Click "Move Up" button to move up/North.\n'
            'Click "Move Right" button to move right/East.\n'
            'Click "Move Down" button to move down/South.\n'
            'Click "Move Left" button to move left/West.\n\n'
            'Answer questions by selecting the radio '
            'button next to correct answer(s) and '
            'clicking the continue button.'
        )


if __name__ == '__main__':
    trivia_game = TriviaMazeGUI()
    trivia_game.run()
