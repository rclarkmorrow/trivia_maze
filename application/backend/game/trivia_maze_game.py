# import the Maze class
from game.player.player_factory import PlayerFactory
from game.maze.maze import Maze

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
        self.__maze = Maze(row_count, col_count)  # Use a maze factory?
        self.__player = PlayerFactory.create_player(player_name)
        self.__rows = row_count
        self.__columns = col_count
        self.__entrance = self.__maze.entrance_pos  # List coordinates
        self.__exit = self.__maze.exit_pos  # List coordinates
        self.__current_room = self.__entrance  # List coordinates
        self.__cheat_mode = False
        self.__questions = questions

    @property
    def maze(self):
        """ Return maze as property. """
        return self.__maze

    @property
    def player(self):
        """ Return player as property. """
        return self.__player

    @property
    def rows(self):
        """ Return row count as property. """
        return self.__rows

    @property
    def columns(self):
        """ Return column count as property. """
        return self.__columns

    @property
    def entrance(self):
        """ Return maze entrance coordinates as property. """
        return self.__entrance

    @property
    def exit(self):
        """ Return maze exit coordinates as property. """
        return self.__exit

    @property
    def current_room(self):
        """ Return current room as property. """
        return self.__current_room

    @current_room.setter
    def current_room(self, current_room):
        """ Set the current room to a new value. """
        self.__current_room = current_room

    @property
    def cheat_mode(self):
        """ Return cheat most enabled status as property. """
        return self.__cheat_mode

    @cheat_mode.setter
    def cheat_mode(self, toggle: bool):
        """ Set cheat mode enabled status. """
        self.__cheat_mode = toggle

    @property
    def questions(self):
        """ Return questions list as property. """
        return self.__questions


if __name__ == '__main__':
    test_game = TriviaMazeGame('Hello World', 4, 4, [1, 2, 3])
    print(test_game.player.name)
