# System imports
import unittest
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.room.room_factory import RoomFactory  # noqa
from game.room.room import Room  # noqa


class RoomTests(unittest.TestCase):
    """ Unit Tests for Room and RoomFactory classes. """

    def test_factory_create_room_no_args(self):
        """ Room is created with no arguments. """

        room = RoomFactory.create_room()

        self.assertTrue(isinstance(room, Room))
        self.assertTrue(room.position is None)
        self.assertTrue(room.features is None)
        self.assertTrue(not room.is_entrance)
        self.assertTrue(not room.is_exit)
        self.assertTrue(room.up is None)
        self.assertTrue(room.right is None)
        self.assertTrue(room.down is None)
        self.assertTrue(room.left is None)
        self.assertTrue(not room.visited)
        self.assertTrue(not room.blocked)

    def test_factory_create_room_position(self):
        """ Room is created with position argument. """

        room = RoomFactory.create_room([6, 2])

        self.assertTrue(isinstance(room, Room))
        self.assertTrue(room.position == [6, 2])
        self.assertTrue(room.features is None)
        self.assertTrue(not room.is_entrance)
        self.assertTrue(not room.is_exit)
        self.assertTrue(room.up is None)
        self.assertTrue(room.right is None)
        self.assertTrue(room.down is None)
        self.assertTrue(room.left is None)
        self.assertTrue(not room.visited)
        self.assertTrue(not room.blocked)

    def test_factory_create_room_bad_position(self):
        """ TypeError when room created with bad position. """
        try:
            _ = RoomFactory.create_room('I am not a list.')
            self.assertEqual(True, False, 'should not have got here: '
                             'room created with non list position.')
        except TypeError:
            self.assertEqual(True, True)

    def test_factory_create_room_wrong_size_list(self):
        """ TypeError when room created with list length != 2. """
        try:
            _ = RoomFactory.create_room([2, 4, 6])
            self.assertEqual(True, False, 'should not have got here: '
                             'room created with list of incorrect length.')
        except TypeError:
            self.assertEqual(True, True)

    def test_factory_create_room_bad_index(self):
        """ TypeError when room created with non-integer index. """
        try:
            _ = RoomFactory.create_room([2, 'I am not an integer.'])
            self.assertEqual(True, False, 'should not have got here: '
                             'room created with non-integer index.')
        except TypeError:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
