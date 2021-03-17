# System imports
import unittest
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.room.room_factory import RoomFactory  # noqa
from game.room.room import Room, Feature  # noqa


class RoomTests(unittest.TestCase):
    """ Unit Tests for Room and RoomFactory classes. """

    """"-------------------------------------------------- #
    #  ROOM FACTORY TESTS                                  #
    #----------------------------------------------------"""

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

    def test_factory_create_room_position_no_features(self):
        """ Room is created with position argument. """

        room = RoomFactory.create_room([6, 2])

        self.assertTrue(isinstance(room, Room))
        self.assertEqual([6, 2], room.position)
        self.assertTrue(room.features is None)
        self.assertTrue(not room.is_entrance)
        self.assertTrue(not room.is_exit)
        self.assertTrue(room.up is None)
        self.assertTrue(room.right is None)
        self.assertTrue(room.down is None)
        self.assertTrue(room.left is None)
        self.assertTrue(not room.visited)
        self.assertTrue(not room.blocked)

    def test_factory_create_room_features_no_position(self):
        """ Room is created with position argument. """
        features = []
        for feature in range(4):
            features.append(Feature())

        room = RoomFactory.create_room(features=features)

        self.assertTrue(isinstance(room, Room))
        self.assertTrue(room.position is None)
        self.assertEqual(features, room.features)
        self.assertEqual(4, len(room.features))
        self.assertTrue(not room.is_entrance)
        self.assertTrue(not room.is_exit)
        self.assertTrue(room.up is None)
        self.assertTrue(room.right is None)
        self.assertTrue(room.down is None)
        self.assertTrue(room.left is None)
        self.assertTrue(not room.visited)
        self.assertTrue(not room.blocked)

    def test_factory_create_room_position_and_features(self):
        """ Room is created with position argument. """
        features = []
        for feature in range(4):
            features.append(Feature())

        room = RoomFactory.create_room(position=[6, 2], features=features)

        self.assertTrue(isinstance(room, Room))
        self.assertEqual([6, 2], room.position)
        self.assertEqual(features, room.features)
        self.assertTrue(not room.is_entrance)
        self.assertTrue(not room.is_exit)
        self.assertTrue(room.up is None)
        self.assertTrue(room.right is None)
        self.assertTrue(room.down is None)
        self.assertTrue(room.left is None)
        self.assertTrue(not room.visited)
        self.assertTrue(not room.blocked)

    def test_factory_create_room_non_list_position(self):
        """ TypeError when room created with non-list position. """
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

    def test_factory_create_room_string_index(self):
        """ TypeError when room created with non-integer index. """
        try:
            _ = RoomFactory.create_room([2, 'I am not an integer.'])
            self.assertEqual(True, False, 'should not have got here: '
                             'room created with non-integer index.')
        except TypeError:
            self.assertEqual(True, True)

    def test_factory_create_room_float_index(self):
        """ TypeError when room created with float index. """
        try:
            _ = RoomFactory.create_room([2, 4.0])
            self.assertEqual(True, False, 'should not have got here: '
                             'room created with non-integer index.')
        except TypeError:
            self.assertEqual(True, True)

    def test_factory_create_room_features_not_list(self):
        """ TypeError when room created with non-list features. """
        try:
            _ = RoomFactory.create_room(features='i am not a list.')
            self.assertEqual(True, False, 'should not have got here: '
                                          'room created with non list '
                                          'features.')
        except TypeError:
            self.assertEqual(True, True)

    def test_factory_create_room_list_of_non_features(self):
        """ TypeError when room created with list of non features. """
        try:
            _ = RoomFactory.create_room(features=[2.0, 4, 'i am not a '
                                                          'feature'])
            self.assertEqual(True, False, 'should not have got here: '
                                          'room created with list of '
                                          'non features.')
        except TypeError:
            self.assertEqual(True, True)

    """"-------------------------------------------------- #
    #  ROOM TESTS                                          #
    #----------------------------------------------------"""

    def test_room_has_no_position_on_create(self):
        """ Room has no position on create. """
        room = Room(position=None, features=None)
        self.assertEqual(None, room.position)

    def test_room_has_position(self):
        """ Room has position when created. """
        room = Room([0, 0], features=None)
        self.assertEqual([0, 0], room.position)

    def test_room_cant_set_position(self):
        """ Rooms returns AttributeError when position updated. """
        room = Room([0, 0], features=None)
        try:
            room.position = [1, 2]
            self.assertEqual((True, False, 'should not have got here:'
                              'was able to set room position'))
        except AttributeError:
            self.assertEqual(True, True)

    def test_room_features_are_none_on_create(self):
        """ Room features are None on create. """
        room = Room([0, 0], features=None)

        self.assertTrue(not room.features)

    def test_room_has_features_on_create(self):
        """ Room has features on create. """
        features = []
        for feature in range(4):
            features.append(Feature())
        room = Room(position=None, features=features)

        self.assertEqual(features, room.features)
        self.assertEqual(4, len(room.features))

    def test_room_add_feature(self):
        """ Room add_feature adds feature. """
        feature = Feature()
        room = Room(position=None, features=[feature])
        room.add_feature(feature)

        self.assertEqual([feature, feature], room.features)

    def test_add_features_bad_feature(self):
        """ TypeError when add_feature passed non Feature. """
        room = Room([0, 0], features=None)
        try:
            room.add_feature('I am not a feature,')
            self.assertEqual(True, False, 'should not have got here: was able'
                                          ' to add non-feature to features')
        except TypeError:
            self.assertEqual(True, True)

    def test_remove_feature(self):
        """ Room remove_feature removes featrue. """
        feature = Feature()
        room = Room(position=[0, 0], features=[feature])
        room.remove_feature(feature)

        self.assertEqual([], room.features)

    def test_remove_feature(self):
        """ TypeError when remove_feature passed non feature. """
        feature = Feature()
        room = Room(position=[0, 0], features=[feature])
        try:
            room.remove_feature('i am not a feature')
            self.assertEqual(True, False, 'should not have got here: was able'
                                          ' to pass non-feature to remove '
                                          'feature')
        except TypeError:
            self.assertEqual(True, True)

    def test_room_is_entrance_is_false_on_create (self):
        """ Room is not entrance on create. """
        room = Room(position=None, features=None)
        self.assertEqual(False, room.is_entrance)

    def test_room_set_entrance_true(self):
        """ Room is_entrance can be set to true. """
        room = Room(position=None, features=None)
        room.is_entrance = True

        self.assertEqual(True, room.is_entrance)

    def test_room_set_entrance_false(self):
        """ Room is_entrance can be set to false. """
        room = Room(position=None, features=None)
        room.is_entrance = True
        room.is_entrance = False

        self.assertEqual(False, room.is_entrance)

    def test_room_is_exit_is_false_on_create(self):
        """ Room is not exit on create. """
        room = Room(position=None, features=None)
        self.assertEqual(False, room.is_exit)

    def test_room_set_exit_true(self):
        """ Room is_exit can be set to true. """
        room = Room(position=None, features=None)
        room.is_exit = True

        self.assertEqual(True, room.is_exit)

    def test_room_set_exit_false(self):
        """ Room is_exit can be set to false. """
        room = Room(position=None, features=None)
        room.is_exit = True
        room.is_exit = False

        self.assertEqual(False, room.is_exit)

    def test_room_visited_is_false_on_create(self):
        """ Room is not visited on create. """
        room = Room(position=None, features=None)
        self.assertEqual(False, room.visited)

    def test_room_set_visited_true(self):
        """ Room visited can be set to true. """
        room = Room(position=None, features=None)
        room.visited = True

        self.assertEqual(True, room.visited)

    def test_room_set_visited_false(self):
        """ Room visited can be set to false. """
        room = Room(position=None, features=None)
        room.visited = True
        room.visited = False

        self.assertEqual(False, room.visited)

    def test_room_blocked_is_false_on_create(self):
        """ Room is not blocked on create. """
        room = Room(position=None, features=None)
        self.assertEqual(False, room.visited)

    def test_room_set_blocked_true(self):
        """ Room blocked can be set to true. """
        room = Room(position=None, features=None)
        room.blocked = True

        self.assertEqual(True, room.blocked)

    def test_room_set_blocked_false(self):
        """ Room blocked can be set to false. """
        room = Room(position=None, features=None)
        room.blocked = True
        room.blocked = False

        self.assertEqual(False, room.blocked)

    def test_room_up_is_none_on_create(self):
        """ Room up is None on create. """
        room = Room(position=None, features=None)
        self.assertEqual(None, room.up)

    def test_room_can_set_up_to_room(self):
        """ Can set up to room. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.up = linked_room

        self.assertEqual(linked_room, room.up)

    def test_room_can_set_up_to_none(self):
        """ Room up can be set to None. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.up = linked_room
        room.up = None

        self.assertEqual(None, room.up)

    def test_room_cant_set_up_to_non_room(self):
        """ Room up can't be set to non-room. """
        room = Room(position=None, features=None)
        try:
            room.up = 'i am not a room'
            self.assertEqual(True, False, 'should not have got here: room up'
                                          ' set to non-room.')
        except TypeError:
            self.assertEqual(True, True)

    def test_room_right_is_none_on_create(self):
        """ Room right is None on create. """
        room = Room(position=None, features=None)
        self.assertEqual(None, room.right)

    def test_room_can_set_right_to_room(self):
        """ Can set right to room. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.right = linked_room

        self.assertEqual(linked_room, room.right)

    def test_room_can_set_right_to_none(self):
        """ Room right can be set to None. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.right = linked_room
        room.right = None

        self.assertEqual(None, room.right)

    def test_room_cant_set_right_to_non_room(self):
        """ Room right can't be set to non-room. """
        room = Room(position=None, features=None)
        try:
            room.right = 'i am not a room'
            self.assertEqual(True, False, 'should not have got here: room up'
                                          ' set to non-room.')
        except TypeError:
            self.assertEqual(True, True)

    def test_room_down_is_none_on_create(self):
        """ Room down is None on create. """
        room = Room(position=None, features=None)
        self.assertEqual(None, room.down)

    def test_room_can_set_down_to_room(self):
        """ Can set down to room. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.down = linked_room

        self.assertEqual(linked_room, room.down)

    def test_room_can_set_down_to_none(self):
        """ Room down can be set to None. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.down = linked_room
        room.down = None

        self.assertEqual(None, room.down)

    def test_room_cant_set_down_to_non_room(self):
        """ Room down can't be set to non-room. """
        room = Room(position=None, features=None)
        try:
            room.down = 'i am not a room'
            self.assertEqual(True, False, 'should not have got here: room up'
                                          ' set to non-room.')
        except TypeError:
            self.assertEqual(True, True)

    def test_room_left_is_none_on_create(self):
        """ Room let is None on create. """
        room = Room(position=None, features=None)
        self.assertEqual(None, room.left)

    def test_room_can_set_left_to_room(self):
        """ Can set left to room. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.left = linked_room

        self.assertEqual(linked_room, room.left)

    def test_room_can_set_left_to_none(self):
        """ Room let can be set to None. """
        room = Room(position=None, features=None)
        linked_room = Room(position=None, features=None)
        room.left = linked_room
        room.left = None

        self.assertEqual(None, room.left)

    def test_room_cant_set_left_to_non_room(self):
        """ Room left can't be set to non-room. """
        room = Room(position=None, features=None)
        try:
            room.left = 'i am not a room'
            self.assertEqual(True, False, 'should not have got here: room up'
                                          ' set to non-room.')
        except TypeError:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
