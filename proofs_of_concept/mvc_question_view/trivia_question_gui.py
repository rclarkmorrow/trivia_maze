import tkinter as Tk
from trivia_game_interface import TriviaGameInterface
from playsound import playsound

FONT = ('Arial', 14)
BGB = 'black'
BGY = 'yellow'
FGG = 'green'
FGY = 'yellow'
BGW = 'white'
FGB = 'black'


class QuestionView:
    """
      This class is an example view that handles displaying questions
      and answers from the database. It initializes with a question,
      but subsequent changes to the question are handled externally by
      the controller view.
    """
    def __init__(self, master, question):
        """
          Initialize the view with a frame, question text as a label
          and a fame for radio buttons and pack.
          :param: master (the parent frame/view)
          :param: question (initial question for view)
        """
        # On initialization create and pack a frame for
        # the view.
        self.frame = Tk.Frame(master, bg=BGB)
        self.frame.pack(side=Tk.TOP)
        self.question = question
        self.user_answer = None
        self.question_text = Tk.Label(
            self.frame,
            text=self.question['Question'],
            wraplength=450,
            justify=Tk.LEFT,
            font=FONT,
            fg=FGY,
            bg=BGB
        )
        self.question_text.pack(side=Tk.TOP)
        self.answer_frame = Tk.Frame(self.frame, bg=BGB)
        self.answer_frame.pack(side=Tk.TOP)
        self.update_answers(init=True)
        self.submit_but = Tk.Button(
            self.frame,
            text='Submit',
            font=FONT,
            bg=BGB,
            fg=BGB
        )
        self.submit_but.pack(side=Tk.RIGHT, anchor='w')

    def update_answers(self, init=False):
        """
          Refreshes list of answers to a question. Uses
          the current self.question variable to display answers.
        """
        def on_change(event=None):
            """
             This method retrieves the user selected radio button,
             and assigns its value to the view's user answer.
            """
            self.user_answer = [self.radio_selection.get()]
            print(f'Answer on change: {self.user_answer}')

        # On initialization set a list of radio buttons to empty.
        if init:
            self.radio_buttons = []
        # On update after initialization destroy previous buttons.
        else:
            for button in self.radio_buttons:
                button.destroy()

        print(f'Answers: {self.question["Answers"]}')
        print(f'Correct: {self.question["Correct"]}')
        # Initialize variable to hold user selected answer
        self.radio_selection = Tk.StringVar()
        self.radio_selection.set('z')
        for key, value in self.question['Answers'].items():
            button = Tk.Radiobutton(
                self.answer_frame,
                text=value,
                variable=self.radio_selection,
                value=key,
                indicatoron=True,
                font=FONT,
                padx=40,
                fg=FGY,
                bg=BGB,
                command=on_change
            )
            button.pack(side=Tk.TOP, anchor="w")
            self.radio_buttons.append(button)
        self.answer_frame.update()

    def update_question(self, question):
        """
          Method updates the question label. It gets passed
          a new question from the parent/controller view.
        """
        self.question = question
        self.question_text.configure(
            text=self.question['Question']
            )
        self.question_text.update()


class Trivia:
    """
      This is the main view/controller of subviews that will
      run the trivia application.
    """
    def __init__(self):
        """
        This method initializes variables.
        """
        self.root = Tk.Tk()
        self.root.geometry('500x300')
        self.root['background'] = BGB
        self.game = TriviaGameInterface()
        self.question_view = QuestionView(self.root,
                                          self.game.question)
        self.question_view.submit_but.bind('<Button>',
                                           self.is_correct)

    def is_correct(self, event=None):
        """
         This runs when the question view button to submit an
         answer is pressed.
        """

        print('button clicked')
        print(f'Answer in is_correct: {self.question_view.user_answer}')
        if (self.question_view.user_answer ==
                self.question_view.question['Correct']):
            self.root.title('CORRECT ANSWER')
            playsound('applause7.mp3')
            print("CORRECT ANSWER")
        else:
            self.root.title('WRONG ANSWER')
            playsound('boo3.mp3')
            print("WRONG!!")
        # The only thing the question view needs is a new question, so
        # the view controller gets a question from the game object
        # (self.game.question) -- and then asks the question view to
        # update it's current question, and then update the answers
        # to that question in the view.
        self.question_view.update_question(self.game.question)
        self.question_view.update_answers()

    def run(self):
        """
          Runs the main application loop.
        """
        self.root.title('MVC Trivia Question Example')
        self.root.deiconify()
        self.root.mainloop()


if __name__ == "__main__":
    trivia_gui = Trivia()
    trivia_gui.run()
