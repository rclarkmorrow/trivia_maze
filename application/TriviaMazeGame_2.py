import tkinter as tk
from tkinter import messagebox
import pickle
from tkinter.constants import S, W
from playsound import playsound
from trivia_game_interface import TriviaGameInterface

FONT = ('Arial', 14)
H_FONT=('Arial', 18)
BGB = 'black'
BGY = 'yellow'
FGG = 'green'
FGY = 'yellow'
BGW = 'white'
FGB = 'black'


class QuestionView(tk.Frame):
    def __init__(self, master=None):
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
            # width=35,
            text='QUESTION',
            wraplength=220,
            fg=FGY,
            bg=BGB)
        self.question_view_title.grid(row=0, column=0, rowspan=2, sticky='nsew')
        self.submit = tk.Button(
            self,
            text='Submit',
            font=FONT,
            bg=BGB,
            fg=BGB,
            wraplength=220,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.submit.grid(row=8, column=0, rowspan=2, sticky='e')
        self.load_question()

    @property
    def __inactive_question(self):
        return {
            'Question': ('No active question, please attempt to move to '
                         'another room to receive a question.'),
            'Answers': {
                'a': '',
                'b': '',
                'c': '',
                'd': ''
            },
            'Correct': ['c']
        }

    def on_change(self):
        """
            This method retrieves the user selected radio button,
            and assigns its value to the view's user answer.
        """
        self.user_answer = [self.radio_selection.get()]

    def load_question(self, question=None):
        """ Loads a new question, or the inactive placeholder """

        if not question:
            self.question = self.__inactive_question
            self.submit['state'] = tk.DISABLED
        else:
            self.question = question
            self.submit['state'] = tk.NORMAL
        
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
        self.question_text.destroy()
        for answer in self.radio_buttons:
            answer.destroy()


class MazeView(tk.Frame):
    def __init__(self, master=None, rows=4, columns=4, 
                 start_position=None, exit_position=None):
        tk.Frame.__init__(self, master=master)
        self.rooms = {}
        self.start_position = start_position
        self.exit_position = exit_position
        self.player_image = tk.PhotoImage(file="Player.png")
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
                    'door_down': door_down
                }
        self.add_player(self.start_position)
        self.add_exit(self.exit_position)

    def move_player(self, old_position, new_position):
        """ Moves players"""
        row, col = old_position
        self.rooms[row, col]['room_center'].delete(self.player)
        row, col = new_position
        self.player = self.rooms[row, col]['room_center'].create_image(
            50,
            70,
            image=self.player_image,
            anchor=tk.SE
        )

    def load_maze(self, maze):
        """
          Loads maze state from game interface and redraws the
          maze on the GUI.
          :param maze: A maze object
        """
        for row in range(maze.row_count):
            for col in range(maze.col_count):

                if col < maze.col_count - 1:
                    if not maze.grid[row][col].right:
                        self.rooms[row, col]['door_right'].config(bg='red')
                if row < maze.row_count - 1:
                    if not maze.grid[row][col].down:
                        self.rooms[row, col]['door_down'].config(bg='red')

    def add_player(self, player_position):
        row, col = player_position
        self.player = self.rooms[row, col]['room_center'].create_image(
            50,
            70,
            image=self.player_image,
            anchor=tk.SE
        )

    def delete_player(self, player_position):
        row, col = player_position
        self.rooms[row, col]['room_center'].delete(self.player)

    def add_exit(self, exit_position):
        row, col = exit_position
        self.exit = self.rooms[row, col]['room_center'].create_image(
            75,
            70,
            image=self.exit_image,
            anchor=tk.SE
        )

    def delete_exit(self, exit_position):
        row, col = exit_position
        self.rooms[row, col]['room_center'].delete(self.exit)


class InfoView(tk.Frame):
    def __init__(self, master=None, text=None):
        tk.Frame.__init__(self, master=master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.label = tk.Label(self, text=text, bg=BGB, fg=FGY)
        self.label.grid(row=0, column=0, sticky='nsew')


class RoomView(tk.Frame):
    def __init__(self, master=None, current_room=None):
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
        self.room_label = tk.Label(
            self.room,
            text=f'{row}, {col}',
            font='Arial 50 bold',
            bg=BGB,
            fg=FGY,
        )
        self.room_label.grid(row=0, column=0, sticky='nsew')

        self.right = tk.Button(
            self,
            text='Move Right',
            font=FONT,
            bg=BGB,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.right.grid(row=1, column=2, sticky='w')

        self.up = tk.Button(
            self,
            text='Move Up',
            font=FONT,
            bg=BGB,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.up.grid(row=0, column=1, sticky='s')
        self.down = tk.Button(
            self,
            text='Move Down',
            font=FONT,
            bg=BGB,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.down.grid(row=2, column=1, sticky='n')

        self.left = tk.Button(
            self,
            text='Move Left',
            font=FONT,
            bg=BGB,
            fg=BGB,
            highlightbackground=BGB,
            highlightcolor=BGB
        )
        self.left.grid(row=1, column=0, sticky='w')

        self.check_exits()

    def check_exits(self):
        if not self.current_room.up:
            self.up['state'] = tk.DISABLED
        else:
            self.up['state'] = tk.NORMAL

        if not self.current_room.right:
            self.right['state'] = tk.DISABLED
        else:
            self.right['state'] = tk.NORMAL
        if not self.current_room.down:
            self.down['state'] = tk.DISABLED
        else:
            self.down['state'] = tk.NORMAL
        if not self.current_room.left:
            self.left['state'] = tk.DISABLED
        else:
            self.left['state'] = tk.NORMAL

    def update_room(self, current_room=None):
        if current_room:
            self.current_room = current_room
        row, col = self.current_room.position
        self.room_label.config(text=f'{row}, '
                               f'{col}')
        self.room_label.update()
        self.check_exits()

    def disable_buttons(self):
        self.up['state'] = tk.DISABLED
        self.right['state'] = tk.DISABLED
        self.down['state'] = tk.DISABLED
        self.left['state'] = tk.DISABLED


class TriviaMazeGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('900x750')
        self.config(bg=BGB)
        self.game = TriviaGameInterface('Jim', 4, 4)
        self.mod_row = None
        self.mod_col = None
        # Create 10 rows and 5 columns
        for row in range(10):
            self.rowconfigure(row, weight=1, minsize=60)
        for col in range(5):
            self.columnconfigure(col, weight=1, minsize=160)
        # Create views and put in grids.
        self.maze_view = MazeView(master=self, rows=4, columns=4,
                                  start_position=self.game.maze_entrance,
                                  exit_position=self.game.maze_exit)
        self.room_view = RoomView(master=self,
                                  current_room=self.game.current_room)
        self.info_view = InfoView()
        self.question_view = QuestionView(master=self)
        # Grid is 10 x 5, row, column = start position,
        # spans = number of cells to cover.
        self.maze_view.grid(row=0, column=0, rowspan=6,
                            columnspan=3, sticky='nsew')
        self.room_view.grid(row=0, column=3, columnspan=2,
                            rowspan=5, sticky='nsew')
        self.info_view.grid(row=6, column=0, columnspan=3,
                            rowspan=4, sticky='nsew')
        self.question_view.grid(row=5, column=3, columnspan=2,
                                rowspan=5, sticky='n')
        # Add menus.
        self.create_menus()

        self.question_view.submit.config(command=self.answer_question)
        self.room_view.up.config(command=self.move_up)
        self.room_view.right.config(command=self.move_right)
        self.room_view.down.config(command=self.move_down)
        self.room_view.left.config(command=self.move_left)
        self.toggle = False

        self.correct_answer = "YES"

    def answer_question(self):
        if self.question_view.user_answer:
            if (self.question_view.user_answer ==
                    self.question_view.question['Correct']):
                playsound('applause7.mp3')
                self.finish_player_move()
            else:
                # Do block doorway
                playsound('boo3.mp3')
                self.answer_incorrect()

    def start_player_move(self):
        self.question_view.reset_question()
        self.question_view.load_question(question=self.game.get_question())
        self.room_view.disable_buttons()

    def finish_player_move(self):
        # Set current player position row and column.
        row, col = self.game.player_position
        # Conditionally modify new row and column.
        new_row = row + self.mod_row if self.mod_row else row
        new_col = col + self.mod_col if self.mod_col else col
        # Move the player icon.
        self.maze_view.move_player([row, col], [new_row, new_col])
        # Update current player position.
        self.game.player_position = ([new_row, new_col])
        # Retrieve the new room details.
        new_room = self.game.current_room
        # Update the room view.
        self.room_view.update_room(new_room)
        self.question_view.reset_question()
        self.question_view.load_question()
        self.mod_row = None
        self.mod_col = None
        # Check win conditions.
        if new_room.is_exit:
            self.win_game()

    def answer_incorrect(self):
        self.room_view.update_room()
        self.question_view.reset_question()
        self.question_view.load_question()

        # Set current player position row and column.
        row, col = self.game.player_position
        # Conditionally modify new row and column.
        new_row = row + self.mod_row if self.mod_row else row
        new_col = col + self.mod_col if self.mod_col else col

        # Check direction player attempted to move and remove
        # doorways.
        if self.mod_row == -1:
            self.game.current_room.up.down = None
            self.game.current_room.up = None
            door_down = self.maze_view.rooms[new_row, col]['door_down']
            door_down.config(bg='red')
        if self.mod_col == 1:
            self.game.current_room.right.left = None
            self.game.current_room.right = None
            door_down = self.maze_view.rooms[row, col]['door_right']
            door_down.config(bg='red')
        if self.mod_row == 1:
            self.game.current_room.down.up = None
            self.game.current_room.down = None
            door_down = self.maze_view.rooms[row, col]['door_down']
            door_down.config(bg='red')
        if self.mod_col == -1:
            self.game.current_room.left.right = None
            self.game.current_room.left = None
            door_down = self.maze_view.rooms[row, new_col]['door_right']
            door_down.config(bg='red')
        self.mod_row = None
        self.mod_col = None
        self.room_view.update_room(self.game.current_room)
        if not self.game.check_path_to_exit():
            self.lose_game()

    def move_up(self):
        self.mod_row = -1
        self.start_player_move()

    def move_right(self):
        self.mod_col = 1
        self.start_player_move()

    def move_down(self):
        self.mod_row = 1
        self.start_player_move()

    def move_left(self):
        self.mod_col = -1
        self.start_player_move()

    def win_game(self):
        msg_box = messagebox.askquestion('Result',
                                         ' CONGRATULATIONS ! YOU WON \n '
                                         'Would you like to play another '
                                         'game ?',
                                         icon='info')
        if msg_box == 'yes':
            self.new_game()
        if msg_box == 'no':
            self.exit_game()

    def lose_game(self):
        msg_box = messagebox.askquestion('Result',
                                         ' You LOST.  Would you like to '
                                         'play another game ?',
                                         icon='info')
        if msg_box == 'yes':
            self.new_game()
        if msg_box == 'no':
            self.exit_game()

    def run(self):
        self.title("TRIVIA MAZE")
        self.mainloop()

    """
    Menus
    """

    def create_menus(self):
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
        file_menu.add_command(label='Exit', command=self.exit_game)
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
        The method is to save the game
        When the save game button is pressed this code needs to be executed
        """
        filename = '../../backend/save_game.pkl'
        status, _ = self.game.save(filename)
        if status:
            header = 'GAME SAVED'
            message = 'Game was successfully saved.'
        else:
            header = 'GAME NOT SAVED'
            message = 'Something went wrong, your game was not saved.'
        messagebox.showinfo(header,
                            message,
                            icon=None)


    def load_game(self):
        """
        This method is used to load the game.

        """

        # Remove player, and exit from mazeview
        self.maze_view.delete_player(self.game.player_position)
        self.maze_view.delete_exit(self.game.maze_exit)
        # Load the game
        filename = "../../backend/save_game.pkl"
        status, _ = self.game.load(filename)
        # Setup views
        self.question_view.load_question()
        self.room_view.update_room(self.game.current_room)
        self.maze_view.load_maze(self.game.game.maze)
        self.maze_view.add_player(self.game.player_position)
        self.maze_view.add_exit(self.game.maze_exit)

        if status:
            header = 'GAME LOADED'
            message = 'Game was successfully loaded.'
        else:
            header = 'GAME NOT LOADED'
            message = 'Something went wrong, your game was not loaded.'
        messagebox.showinfo(header,
                            message,
                            icon=None)

    def new_game(self):
        """
        This method is used to start a new game
         """
        self.destroy()
        trivia_game = TriviaMazeGUI()
        trivia_game.run()

    def exit_game(self):
        self.destroy()

    def about_us(self):
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

    def game_instructions(self):
        """
        This method displays the game instructions
        """
        messagebox.showinfo(
            'Instructions',
            'Trivia Maze Game Instructions:\n\n'
            'Your goal is to reach the exit of the maze '
            'by successfully answering questions to gain '
            'entrance to a new room. Answering a question '
            'incorrectly will block a door from entry.\n\n'
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
