# System imports
import pickle
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[0]
sys.path.append((str(package_root_directory)))
from game.trivia_maze_game import TriviaMazeGame  # noqa
from database.triviamazedb import TriviaMazeDB  # noqa


class TriviaGameInterface:
    def __init__(self, player_name, row_count, col_count):
        question_list = TriviaMazeDB.get_question_list(row_count * col_count)
        self.__game = TriviaMazeGame(player_name, row_count,
                                     col_count, question_list)

    @property
    def game(self):
        """ Returns game object as property. """
        return self.__game

    @property
    def maze_entrance(self):
        """ Returns maze entrance as a property. """
        return self.__game.entrance  # [x, y]

    @property
    def maze_exit(self):
        """ returns maze exit as a property. """
        return self.__game.exit

    @property
    def current_room(self):
        """ returns the room object at player position. """
        row, col = self.__game.player_position
        return self.__game.maze.grid[row][col]

    @property
    def player_position(self):
        """ Returns the player's position as a property. """
        return self.__game.player_position

    @player_position.setter
    def player_position(self, player_position):
        self.__game.player_position = player_position

    @property
    def current_question(self):
        return self.__game.current_question

    def check_path_to_exit(self):
        return self.__game.maze.can_reach_exit(self.__game.player_position)

    def get_question(self):
        """
          Tries to get a question from the game object,
          returns True with question if successful, False
          with error message if not.
          :Return: True, question
          :Return: False, error
        """
        return self.__game.question

    def save(self, file_name):
        """ Returns results of attempt to save file. """
        return self.__save(file_name)

    def load(self, file_name):
        """ Returns results of attempt to load file. """
        success, result = self.__load(file_name)
        if success:
            self.__game = result
            result = 'game successfully loaded.'
        return success, result

    def __save(self, file_name):
        """
          Method pickles an object and saves to file.
          :Param file_name: name of file to save game to
          :Return: True, message if saved
          :Return: False, error is not saved
        """
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(self.__game, file, protocol=3)
                return True, 'game successfully saved.'
        except Exception as error:
            return False, f'game not saved: {error}.'

    @staticmethod
    def __load(file_name):
        """
          Try to load a pickled game object and return a response
          indicating success for failure.
          :Param file_name: name of the file to open
          :Return: True and game object is successful
          :Return: False and error message if not successful
        """
        try:
            # Load and unpickle using with so the file is closed for us.
            with open(file_name, 'rb') as file:
                loaded_game = pickle.load(file)
                print(f'Loaded: {loaded_game}')
                return True, loaded_game

        except Exception as error:
            return False, f'game not loaded {error}'


if __name__ == '__main__':
    """
      Some basic smoke tests
    """
    test_interface = TriviaGameInterface('player', 4, 4)
    init_player_name = test_interface.game.player.name
    print(f'Player name on init: {init_player_name}')
    result = test_interface.save('test_save.pkl')
    print(f'Save results: {result[0]}, {result[1]}')
    result = test_interface.load('test_save.pkl')
    print(f'Load results: {result[0]}, {result[1]}')
    load_player_name = test_interface.game.player.name
    print(f'Player name on load: {load_player_name}')
    print(f'Names match: {init_player_name == load_player_name}')
    # test_interface.game.block_room([2,2])
    print(f'blocked rooms: {test_interface.game.blocked_rooms}')

