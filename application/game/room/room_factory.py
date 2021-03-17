# System imports
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append((str(package_root_directory)))
from game.room.room import Room, Feature  # noqa


class RoomFactory:
    """
     This class creates instances of a room object.
    """
    # Error messages
    POSITION_ERROR = ('Position must be None or a list of [x, y] '
                      'indices as integers.')
    FEATURES_ERROR = 'Features must be None or a list of Feature instances.'

    @staticmethod
    def create_room(position=None, features=None):
        """
          Creates a room instance.
          :param position: List of [x, y] indices as integers.
          :param features: List of features instances.
        """
        if not RoomFactory.__verify_position(position):
            raise TypeError(RoomFactory.POSITION_ERROR)
        if not RoomFactory.__verify_features(features):
            raise TypeError(RoomFactory.FEATURES_ERROR)
        return Room(position, features)

    @staticmethod
    def __verify_position(position):
        """ Verifies a valid position. """
        # Return true if none.
        if not position:
            return True
        # Check parameter conditions
        if not isinstance(position, list):
            return False
        if len(position) != 2:
            return False
        for index in position:
            if not isinstance(index, int):
                return False
        return True

    @staticmethod
    def __verify_features(features):
        """ Verifies valid list of Features. """
        if not features:
            return True
        if not isinstance(features, list):
            return False
        for feature in features:
            if not isinstance(feature, Feature):
                return False
        return True
