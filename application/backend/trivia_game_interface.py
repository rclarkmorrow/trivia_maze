from pickle import dump, load

from game.trivia_maze_game import TriviaMazeGame
from database.triviamazedb import TriviaMazeDB


class TriviaGameInterface:
    def __init__(self, player_name, row_count, col_count):
        question_list = TriviaMazeDB.get_question_list(row_count * col_count)
        self.__game = TriviaMazeGame(player_name, row_count,
                                     col_count, question_list)

    @property
    def game(self):
        return self.__game

    def save(self, file_name):
        return self.__save(file_name)

    def load(self, file_name):
        success, result = self.__load(file_name)
        if success:
            self.__game = result
            result = 'game successfully loaded.'
        return success, result

    def __save(self, file_name):
        """
          Method pickels an object
        """
        try:
            with open(file_name, 'wb') as file:
                dump(self.__game, file, protocol=3)
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
                loaded_game = load(file)
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
