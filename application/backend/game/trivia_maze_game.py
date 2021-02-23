# import the Maze class
from player.player_factory import PlayerFactory
from maze.maze import Maze

class TriviaMazeGame:
    """
       The TriviaMazeGame class creates a Trivia Maze Game and tracks that
       game's current state so that it can saved to be played later.
    """
    def __init__(self, player_name, row_count, col_count, questions):
        self.__maze = Maze(row_count, col_count)
        self.__player = PlayerFactory.create_player(player_name)
        self.__entrance = self.__maze.entrance_pos
        self.__exit = self.__maze.exit_pos
        self.__current_room = self.__entrance
        self.__cheat_mode = False
        self.__questions = questions

    @property
    def maze(self):
        return self.__maze
    @property
    def player(self):
        return self.__player
    @property
    def current_room(self):
        return self.__current_room
    @property
    def cheat_mode(self):
        return self.__cheat_mode
    @cheat_mode.setter
    def cheat_mode(self, toggle: bool):
        self.__cheat_mode = toggle

    # def toggle_cheat(self):
    #     # Toggle the boolean.
    #     self.__cheat_mode = not self.__cheat_mode
    #     # NOTE: may need to return information about whether
    #     # the cheat mode was enable or disabled here.
    #     return


if __name__ == '__main__':
    test_game = TriviaMazeGame('Hello World', 4, 4, [1, 2, 3])
    print(test_game.player.name)