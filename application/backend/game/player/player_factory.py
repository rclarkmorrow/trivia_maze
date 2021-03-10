# Standard library imports
import sys
import random
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append((str(package_root_directory)))
from game.player.player import Player  # noqa


DEFAULT_NAMES = ['Tom', 'Player']


class PlayerFactory:
    """
      Simple factory class to create and return a player instance.

    """
    @staticmethod
    def create_player(name=random.choice(DEFAULT_NAMES)):
        """
          Returns a Player instance with a provided name or a
          default name.
          :param name: (takes a name for the player as a parameter, defaults
                       to a random selection from the DEFAULT_NAMES constant
                       if none provided).
        """
        if not isinstance(name, str):
            raise TypeError('name must be of type string.')
        return Player(name)
