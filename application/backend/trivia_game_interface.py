from game.trivia_maze_game import TriviaMazeGame
from database.triviamaze.db import TriviaMazeDB

class TriviaGameInterface:
    def __init__(self, player_name, row_count, col_count):
        db_conn = TriviaMazeDB.create_connection()
        # Create a close connection method in the DB
        question_list = TriviaMazeDB.get_question_list(row_count * col_count)
        self.__game = TriviaMazeGame(player_name, row_count,
                                     col_count, question_list)

    @property
    def game (self):
        return self.__game