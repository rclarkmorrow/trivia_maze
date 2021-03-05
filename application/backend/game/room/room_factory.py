# System imports
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append((str(package_root_directory)))
from game.room.room import Room  # noqa


class RoomFactory:
    """
     This class creates instances of a room object.
    """
    # Error messages
    POSITION_ERROR = 'Position must be a list of [x, y] indices as integers.'
    FEATURES_ERROR = 'Features must be a list of Feature instances.'

    @staticmethod
    def create_room(position=None, features=None):
        if not RoomFactory.__verify_position(position):
            raise TypeError(RoomFactory.POSITION_ERROR)
        if not RoomFactory.__verify_features(features):
            raise TypeError(RoomFactory.FEATURES_ERROR)
        return Room(position, features)

    @staticmethod
    def __verify_position(position):
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
        return Trueroom

    @staticmethod
    def __verify_features(features):
        if not features:
            return True
        # Update failure conditionals when features are implemented.
        else:
            return False


if __name__ == '__main__':
    """ Basic smoke tests. """
    room = RoomFactory.create_room()
    print(room)
    room = RoomFactory.create_room([2, 3])
    print(type(room))
    print('\n'.join(room.draw_room()))