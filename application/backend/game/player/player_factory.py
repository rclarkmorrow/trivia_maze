from game.player.player import Player
from random import choice

DEFAULT_NAMES = ['Tom', 'Player']


class PlayerFactory:
    """
      Simple factory class to create and return a player instance.

    """
    @staticmethod
    def create_player(name=choice(DEFAULT_NAMES)):
        """
          Returns a Player instance with a provided name or a
          default name.
          :param name: (takes a name for the player as a parameter, defaults
                       to a random selection from the DEFAULT_NAMES constant
                       if none provided).
        """
        return Player(name)
