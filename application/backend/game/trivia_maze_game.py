# import the MazeFactory
# import the PlayerFactory
# import Question [maybe]

class TriviaMazeGame:
    """
       The TriviaMazeGame class creates a Trivia Maze Game and tracks that
       game's current state so that it can saved to be played later.
    """
    def __init__(self, player_name):
        self.__maze = MazeFactory()
        self.__player = PlayerFactory(player_name)
        self.questions = self.__get_questions()  # Note: get the size of the maze from
                                                 # self.__maze
        self.__current_room = self.__maze.entrance_exit_pos[0]
        self.__cheat_mode = False

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
    def cheat_mode(self, toggle:Bool):
        self.__cheat_mode = toggle

    # def toggle_cheat(self):
    #     # Toggle the boolean.
    #     self.__cheat_mode = not self.__cheat_mode
    #     # NOTE: may need to return information about whether
    #     # the cheat mode was enable or disabled here.
    #     return

    def player_move(self):
        pass
    def player_answer_question(self):
        pass
    def __player_enter_room(self):
        pass
    def __player_question(self):
        pass
    def __get_questions(self):
        # Query database to get a list
        # of random questions of length
        # room count of maze.
        pass

