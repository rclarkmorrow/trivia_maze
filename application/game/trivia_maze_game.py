# System imports
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.player.player_factory import PlayerFactory  # noqa
from game.maze.maze import Maze  # noqa


class TriviaMazeGame:
    """
       The TriviaMazeGame class creates a Trivia Maze Game and tracks that
       game's current state so that it can saved to be played later.
       :Param player_name: The player's name as a string.
       :Param row_count: An integer representing the number
                         of rows in the maze.
       :Param col_count: An integer representing the number
                         of columns in the maze.
    """
    def __init__(self, player_name, row_count, col_count, questions):
        self.__maze = Maze(row_count, col_count)
        self.__player = PlayerFactory.create_player(player_name)
        self.__row_count = row_count
        self.__col_count = col_count
        self.__questions = questions
        self.__current_question = None  # Question
        self.__entrance = self.__maze.entrance  # List coordinates
        self.__exit = self.__maze.exit  # List coordinates
        self.__player_position = self.__entrance  # List coordinates
        self.__visited_rooms = []  # List of lists of coordinates
        self.__blocked_rooms = []  # List of lists of coordinates
        self.__cheat_mode = False


    @property
    def maze(self):
        """ Return maze as property. """
        return self.__maze  # Maze object

    @property
    def player(self):
        """ Return player as property. """
        return self.__player  # Player object

    @property
    def row_count(self):
        """ Return row count as property. """
        return self.__row_count  # Integer of row size

    @property
    def col_count(self):
        """ Return column count as property. """
        return self.__col_count  # Integer of column count

    @property
    def entrance(self):
        """ Return maze entrance coordinates as property. """
        return self.__entrance  # Entrance as [x, y]

    @property
    def exit(self):
        """ Return maze exit coordinates as property. """
        return self.__exit  # Exit [x, y]

    @property
    def player_position(self):
        """ Return current room as property. """
        return self.__player_position  # Room as [x, y]

    @player_position.setter
    def player_position(self, player_position):
        """ Set the current room to a new value. """
        self.__player_position = player_position

    @property
    def visited_rooms(self):
        """ Return visited rooms as property. """
        return self.__visited_rooms  # List [[x, y], [x, y]]

    @property
    def blocked_rooms(self):
        """ Returns blocked rooms list as property. """
        # NOTE: if we block doors instead of rooms, we may not use this
        # or we may change it.
        return self.__blocked_rooms  # List [[x, y], [x, y]]

    @property
    def cheat_mode(self):
        """ Return cheat most enabled status as property. """
        return self.__cheat_mode  # Boolean

    @cheat_mode.setter
    def cheat_mode(self, toggle: bool):
        """ Set cheat mode enabled status. """
        self.__cheat_mode = toggle

    @property
    def questions(self):
        """ Return questions list as property. """
        # NOTE: We may just want to load a new question ever time a
        # player tries to move.
        return self.__questions  # List [question object, question, object]

    @property
    def current_question(self):
        if self.__current_question:
            return self.__current_question.formatted
        else:
            return None

    @property
    def question(self):
        """ Pop a question from list and return it. """
        # NOTE: See above
        if len(self.__questions) > 0:
            self.__current_question = self.__questions.pop()
            return self.__current_question.formatted
        else:
            return None


if __name__ == '__main__':
    test_game = TriviaMazeGame('Hello World', 4, 4, [1, 2, 3])
    print(test_game.player.name)
