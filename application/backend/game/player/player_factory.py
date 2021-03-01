from game.player.player import Player
from random import choice

DEFAULT_NAMES = ['Tom', 'Player']


class PlayerFactory:
    """
      Simple factory class to create and return a player instance.
      :param: name (takes a name for the player as a parameter, defaults
              to a random selection from the DEFAULT_NAMES constant if
              none provided).
    """
    @staticmethod
    def create_player(name=choice(DEFAULT_NAMES)):
        return Player(name)
