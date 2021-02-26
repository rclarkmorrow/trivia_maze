import random
from Room import Room


class RoomFactory:
    """
    The RoomFactory class contains three different methods to create/update rooms for typical inner and edge condition,
    rooms along the traversable path and entrance/exit.
    """
    @staticmethod
    def create_room(row_count: int, col_count: int, max_row_count: int, max_col_count: int,
                    room_content=" "):
        """
        Creates typical rooms and randomly assign doors if the room is not on perimeter. If the room is located along the
        perimeter, use wall instead of door.
        """
        room = Room()
        room_matrix = room.room_matrix  # default room matrix is filled with "*" as walls
        room_matrix[1][1] = room_content
        room_matrix[0][1] = "*" if row_count == 0 or bool(random.getrandbits(1)) else "-"
        room_matrix[1][0] = "*" if col_count == 0 or bool(random.getrandbits(1)) else "|"
        room_matrix[2][1] = "*" if row_count == max_row_count or bool(random.getrandbits(1)) else "_"
        room_matrix[1][2] = "*" if col_count == max_col_count or bool(random.getrandbits(1)) else "|"
        return room

    @staticmethod
    def connect_room(room1: Room, room2: Room, room1_loc: list, room2_loc: list):
        """
        Connects two rooms together such that a player can travel between them.
        """
        dir_x = room2_loc[0] - room1_loc[0]
        dir_y = room2_loc[1] - room1_loc[1]
        if dir_y == 1:
            room1.room_matrix[1][2] = "|"
            room2.room_matrix[1][0] = "|"
        elif dir_y == -1:
            room2.room_matrix[1][2] = "|"
            room1.room_matrix[1][0] = "|"
        elif dir_x == 1:
            room1.room_matrix[2][1] = "-"
            room2.room_matrix[0][1] = "-"
        elif dir_x == -1:
            room2.room_matrix[2][1] = "-"
            room1.room_matrix[0][1] = "-"

    @staticmethod
    def update_room_as_exit(room: Room, row: int, col: int, max_row: int, max_col: int, room_content="O"):
        """
        Updates the designated room to be the exit of the dungeon.
        """
        if row == 0:
            room.room_matrix[0][1] = "-"
        elif row == max_row:
            room.room_matrix[2][1] = "-"
        elif col == 0:
            room.room_matrix[1][0] = "|"
        else:
            room.room_matrix[1][2] = "|"

        room.room_content = room_content


if __name__ == "__main__":
    print(RoomFactory.create_room(0, 0, 5, 5))

