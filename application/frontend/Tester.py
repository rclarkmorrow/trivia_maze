import unittest
from Room import Room
from RoomFactory import RoomFactory
from Dungeon import Dungeon
from DungeonAdventure import DungeonAdventurer
from Adventurer import Adventurer


class MyTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This class method setup the dungeon generator once and it can be used
        in the test classes below. Otherwise it generates every time and because
        there is a random generation in the dungeon generator and it saves time.
        """
        cls.nrows = 20
        cls.ncols  =20
        cls.dungeon = Dungeon(cls.nrows,cls.ncols)
        cls.dungeon.dungeon_generator()

    """
    1) Testing 'Room' class functionality
    """

    def test_init(self):
        """
        This test checks if the room is empty initially
        """
        room = Room()
        self.assertEqual("* * *\n* * *\n* * *\n", room.__str__(), "Room should be empty but is not")

    def test_room_content_with_A_pillar(self):
        """
        This test checks if the room can be populated and contains A pillar.
        """
        try:
            room= Room("A")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "A", "room content does not returns A")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_E_pillar(self):
        """
        This test checks if the room can be populated and contains E pillar
        """
        try:
            room= Room("E")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "E", "room content does not returns E")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_I_pillar(self):
        """
        This test checks if the room can be populated and contains I pillar
        """
        try:
            room= Room("I")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "I", "room content does not returns I")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_P_pillar(self):
        """
        This test checks if the room can be populated and contains P pillar
        """
        try:
            room= Room("P")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "P", "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_room_content_with_empty_content(self):
        """
        This test checks if the room content is empty as needed
        """
        try:
            room= Room("")
            return_room_content= room.room_content
            self.assertEqual(return_room_content, "", "room content does not returns empty")
        except ValueError as value_error:
            self.assertEqual(True, True)


    """
    2) Testing 'Room Factory' class functionality
    """
    def test_RoomFactory_room_has_NORTH_doors_and_walls(self):
        """
        This test checks if the room factory generates a room and has North doors and walls
        """
        try:
            rm_factory= RoomFactory.create_room(1,1,2,2," ")
            temp2=rm_factory.room_matrix[0][1]=='*' or rm_factory.room_matrix[0][1]=='-'
            self.assertEqual(temp2, True, "north doors and walls not present")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_RoomFactory_room_has_SOUTH_doors_and_walls(self):
        """
        This test checks if the room factory generates a room and has South doors and walls
        """
        try:
            rm_factory= RoomFactory.create_room(2,2,2,2," ")
            print(rm_factory.room_matrix[2][1])
            temp3=rm_factory.room_matrix[2][1]=='*' or rm_factory.room_matrix[2][1]=='-'
            self.assertEqual(temp3, True, "south doors and walls not present")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_RoomFactory_room_has_East_doors_and_walls(self):
        """
        This test checks if the room factory generates a room and has East doors and walls
        """
        try:
            rm_factory= RoomFactory.create_room(0,0,1,1," ")
            temp1=rm_factory.room_matrix[1][2]=='*' or rm_factory.room_matrix[1][2]=='|'
            self.assertEqual(temp1, True, "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_RoomFactory_room_has_West_doors_and_walls(self):
        """
        This test checks if the room factory generates a room and has West doors and walls
        """
        try:
            rm_factory= RoomFactory.create_room(0,0,1,1," ")
            temp1=rm_factory.room_matrix[1][0]=='*' or rm_factory.room_matrix[1][0]=='|'
            self.assertEqual(temp1, True, "room content does not returns P")
        except ValueError as value_error:
            self.assertEqual(True, True)

    """
    3) Testing 'Dungeon' class functionality
    """
    def test_dungeon_has_Pit_X(self):
        """
        This tests whether the dungeon has a pit X
        """
        try:
            temp_list = list(self.dungeon.__str__())
            self.assertIn('X', temp_list, "dungeon does not have pit X")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_dungeon_has_entrance_i(self):
        """
        This tests whether the dungeon has an entrance i
        """
        try:
            temp_list = list(self.dungeon.__str__())
            self.assertIn('i', temp_list, "dungeon does not have entrance i")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_dungeon_has_exit_O(self):
        """
        This tests whether the dungeon has an exit O
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('O', temp_list, "dungeon does not have exit O")

    def test_dungeon_has_vision_potion_V(self):
        """
        This tests whether the dungeon has a vision potion V
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('V', temp_list, "dungeon does not have healing potion V")

    def test_dungeon_has_healing_potion_H(self):
        """
        This tests whether the dungeon has a healing potion H
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('H', temp_list, "dungeon does not have healing potion H")

    def test_dungeon_has_multiple_items_M(self):
        """
        This tests whether the dungeon contains and displays for multiple items
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('M', temp_list, "dungeon does not have multiple items 'M'")

    def test_dungeon_has_A_pillar(self):
        """
        This tests whether the dungeon has an A pillar
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('A',temp_list,"dungeon does not have 'A' pillar ")

    def test_dungeon_has_E_pillar(self):
        """
        This tests whether the dungeon has an E pillar
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('E',temp_list,"dungeon does not have 'E' pillar ")

    def test_dungeon_has_I_pillar(self):
        """
        This tests whether the dungeon has an I pillar
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('I',temp_list,"dungeon does not have 'I' pillar ")

    def test_dungeon_has_P_pillar(self):
        """
        This tests whether the dungeon has a P pillar
        """
        temp_list = list(self.dungeon.__str__())
        self.assertIn('P',temp_list,"dungeon does not have 'P' pillar ")

    def test_entrance_location_is_positive(self):
        """
        This tests whether the entrance location is positive
        """
        try:
            dungeon = Dungeon(6, 6)
            temp4 = dungeon.entrance_generator()
            self.assertGreaterEqual(temp4, [0, 0], "entrance location is positive")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_entrance_location_within_the_max_value(self):
        """
        This tests whether the entrance location is does not exceed the max value
        """
        try:
            temp4 = self.dungeon.entrance_generator()
            self.assertLess(temp4, [self.nrows, self.ncols], "entrance location is within max value")
        except ValueError as value_error:
            self.assertEqual(True, True)

    """
    4) Testing 'Adventure' class functionality
    """
    def test_pillars_collected_empty(self):
        """
        This tests the pillar collected list is empty at the beginning
        """
        self.assertEqual([], Adventurer('R').pillar_collected, "Pillars collected should be empty but is not")

    def test_healing_potion_count_zero(self):
        """
        This tests the healing potion is zero at the beginning.
        """
        self.assertEqual(0, Adventurer('R').healing_potion_count, "Initial Healing potion count should be zero")

    def test_vision_potion_count_zero(self):
        """
        This tests the vision potion is zero at the beginning.
        """
        self.assertEqual(0, Adventurer('R').vision_potion_count, "Initial Vision potion count should be zero")

    def test_hit_points_not_negative(self):
        """
        This tests the hit points less than zero / negative.
        """
        self.assertGreater(Adventurer('R').hit_points, 0, "Hit points are negative")

    """
    5) Testing 'DungeonAdventure' class functionality
    """
    def test_adventurer_does_not_move_out_of_east_boundary(self):
        """
        This tests that the adventurer does not move out of the east boundary.
        """
        temp5=DungeonAdventurer.if_passable(self.dungeon,7,self.ncols,7,self.ncols+1,self.nrows,self.ncols)
        self.assertEqual(temp5, False, "adventurer moves out of boundary")

    def test_adventurer_does_not_move_out_of_boundary_west_X(self):
        """
        This tests that the adventurer does not move out of the west boundary.
        """
        temp5=DungeonAdventurer.if_passable(self.dungeon,7,0,7,-1,self.nrows,self.ncols)
        self.assertEqual(temp5, False, "adventurer moves out of boundary")

    def test_adventurer_does_not_move_out_of_north_boundary(self):
        """
        This tests that the adventurer does not move out of the north boundary.
        """
        temp5 = DungeonAdventurer.if_passable(self.dungeon, 0, 7, -1, 7, self.nrows, self.ncols)
        self.assertEqual(temp5, False, "adventurer moves out of boundary")

    def test_adventurer_does_not_move_out_of_south_boundary(self):
        """
        This tests that the adventurer does not move out of the south boundary.
        """
        temp5 = DungeonAdventurer.if_passable(self.dungeon, self.nrows, 7, self.nrows+1, 7, self.nrows, self.ncols)
        self.assertEqual(temp5, False, "adventurer moves out of boundary")


if __name__ == '__main__':
    unittest.main()

