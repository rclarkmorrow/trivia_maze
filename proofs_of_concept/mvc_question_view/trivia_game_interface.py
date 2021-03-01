from triviamazedb import TriviaMazeDB

QUESTION_COUNT = 10


class TriviaGameInterface:
    def __init__(self):
        db = TriviaMazeDB
        conn = db.create_connection()
        self.__questions = db.get_question_list(conn, QUESTION_COUNT)

    @property
    def question(self):
        # question = self.__questions.pop()
        return self.__questions.pop().formatted
        # return question.formatted
