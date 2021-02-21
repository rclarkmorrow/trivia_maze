from tkinter import *
import tkinter as tk


class MoveClicks(object):
    def __init__(self):
        """
        Initialization
        """

        # Tk window

        self.my_window = tk.Tk()
        self.my_window.title('WELCOME TO THE TRIVIA GAME')

        self.window_width = 1100
        self.window_height = 1100

        # Create Canvas
        self.my_canvas = tk.Canvas(master=self.my_window, width=self.window_height, height=self.window_height,
                                   background='black')

        self.my_canvas2 = tk.Canvas(master=self.my_window, width=self.window_height/2, height=self.window_height/2,
                                   background='white')

        # Create player
        self.my_player = self.my_canvas.create_oval(200, 200, 260, 260, fill='purple')
        self.my_player2 = self.my_canvas2.create_oval(200, 200, 260, 260, fill='blue')

        # Location of the mouse click position box (top right corner of the gui layout)
        self.x1 = 800
        self.y1 = 100
        self.x2 = 1000
        self.y2 = 300

    def create_box(self):
        """
        The method creates rooms on canvas
        """

        # Create Box
        self.my_canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="black", outline='white')

        """
        Create mouse/button click events for player movement after answering Trivia
        """
        def left():
            x = -30
            y = 0
            self.my_canvas.move(self.my_player, x, y)

        def right():
            x = 30
            y = 0
            self.my_canvas.move(self.my_player, x, y)

        def up():
            x = 0
            y = -30
            self.my_canvas.move(self.my_player, x, y)

        def down():
            x = 0
            y = 30
            self.my_canvas.move(self.my_player, x, y)

        """
        Create Click Buttons
        """
        # Create West Button
        button1 = Button(self.my_canvas, text="Move Left", font='12',bg='red', fg='white',command=left)
        button1.place(x=self.x1-80, y=(self.y1+self.y2)/2-10)

        # Create East Button
        button2 = Button(self.my_canvas, text="Move Right", font='12', bg='red', fg='white', command=right)
        button2.place(x=self.x1+200,y=(self.y1 + self.y2)/2 -10)

        # Create North Button
        button3 = Button(self.my_canvas, text="Move Up", font='12', bg='red', fg='white', command=up)
        button3.place(x=self.x1+ (self.x2-self.x1)/3,y=self.y1-32)

        # Create South Button
        button3 = Button(self.my_canvas, text="Move Down", font='12', bg='red', fg='white', command=down)
        button3.place(x=self.x1-10+(self.x2-self.x1)/3,y=self.y2)

        self.my_canvas.pack()
        self.my_canvas.update()

    def create_player_location(self):
        """
        Players current room position info
        """
        self.my_canvas.create_text((self.x1+self.x2)/2, (self.y1+self.y2)/2,
                                   text="A", font=("Helvetica", 40), fill='white')

        self.my_canvas.create_text(self.x1, self.y1+30, text="You are currently in \n Room",
                                   font=("Helvetica", 14), fill='red', anchor='w')

    def start(self):
        """
        Start the display
        """
        MoveClicks.create_box(self)
        MoveClicks.create_player_location(self)
        self.my_window.mainloop()


if __name__ == "__main__":
    name = "XYZ"
    move_clicks_gui = MoveClicks()
    move_clicks_gui.start()