import math
import random
from RoomFactory import RoomFactory


class Dungeon:
    """
    This class randomly generates a maze of rooms given the desired dimensions
    which players can pass through to play the Dungeon Adventure game.
    """
    def __init__(self, column_count, row_count):
        """
        Given dungeon dimensions, a dungeon can be constructed with rooms that can contain items for the game.
        """
        self.__column_count = column_count
        self.__row_count = row_count
        self.__room_list = []
        self.__room_content = {"M": 0.1, "X": 0.1, "V": 0.2, "H": 0.2}  # dict of each room content & ratio
        self.__pillar = ["A", "E", "I", "P"]
        self.__room_content_count = None  # number count of each room content
        self.__vision_rooms = []
        self.__entrance_exit_pos = []
        self.__empty_rooms = column_count * row_count - 6

    @property
    def room_content(self):
        """"Gives other classes access to the private field of self.__room_content.keys()."""
        return self.__room_content.keys()

    @property
    def room_list(self):
        """"Gives other classes access to the private field of self.__room_list."""
        return self.__room_list

    def entrance_generator(self):
        """
        Generates the 2d coordinate pair for the entrance by randomly pick one coordinate along the perimeter.

        """
        entrance_x = random.choice([0, self.__row_count - 1])
        entrance_y = random.choice([0, self.__column_count - 1])
        entrance_location = random.choice([[entrance_x, random.randint(0, self.__column_count - 1)],
                                           [random.randint(0, self.__row_count - 1), entrance_y]])
        return entrance_location

    def dungeon_generator(self):
        """
        Generates the dungeon by setting up the entrance point, create_room from RoomFactory class and lists of lists.
        """
        self.cal_room_content()
        # populate empty dungeon without room_content
        for r in range(0, self.__row_count):
            room_row = []
            for c in range(0, self.__column_count):
                room_row.append(RoomFactory.create_room(r, c, self.__row_count - 1, self.__column_count - 1))
            self.__room_list.append(room_row)
        # call set_traverse_path function to set door alignments between rooms
        self.set_traverse_path()
        # assign room_content for empty rooms that are not entrance or exit
        for row in range(0, self.__row_count):
            for column in range(0, self.__column_count):
                room = self.__room_list[row][column]
                if room.room_content is None:
                    room.room_content = self.room_content_generator()
                if room.room_content == "V":
                    self.__vision_rooms.append([row, column])
        self.set_room_vision_potion()
        return self.__room_list

    def set_traverse_path(self):
        """
        Finds a traversable path from the entrance room by randomly picking the moving direction until
        reach the perimeter of the dungeon, which will be the exit room. The method guarantees each generated dungeon is
        valid and has at least one traversable path. Four pillars are assigned along the path as room_content.
        """
        entrance_point = self.entrance_generator()
        RoomFactory.update_room_as_exit(self.__room_list[entrance_point[0]][entrance_point[1]], entrance_point[0],
                                        entrance_point[1], self.__row_count - 1,
                                        self.__column_count - 1, "i")

        self.__entrance_exit_pos.append(entrance_point)
        path_room_list = []
        curr_x = entrance_point[0]
        curr_y = entrance_point[1]
        path_room_list.append(entrance_point)
        while curr_x != 0 and curr_x != self.__row_count - 1 and curr_y != 0 and curr_y != self.__column_count - 1 or [
            curr_x, curr_y] == entrance_point or len(path_room_list) < 6:
            random_dir_generator = random.choice(["W", "S", "E", "N"])
            self.__room_list[curr_x][curr_y].is_visited = True
            if random_dir_generator == "N" and curr_x - 1 >= 0 and not self.__room_list[curr_x][curr_y - 1].is_visited:
                next_room = [curr_x - 1, curr_y]
                path_room_list.append(next_room)
                curr_x -= 1
            elif random_dir_generator == "E" and curr_y + 1 < self.__column_count and self.__room_list[curr_x][
                curr_y + 1].is_visited is False:
                next_room = [curr_x, curr_y + 1]
                path_room_list.append(next_room)
                curr_y += 1
            elif random_dir_generator == "S" and curr_x + 1 < self.__row_count and self.__room_list[curr_x + 1][
                curr_y].is_visited is False:
                next_room = [curr_x + 1, curr_y]
                path_room_list.append(next_room)
                curr_x += 1
            elif random_dir_generator == "W" and curr_y - 1 >= 0 and self.__room_list[curr_x][
                curr_y - 1].is_visited is False:
                next_room = [curr_x, curr_y - 1]
                path_room_list.append(next_room)
                curr_y -= 1
        else:
            self.__entrance_exit_pos.append([curr_x, curr_y])
            for idx in range(len(path_room_list)-1):
                room2_loc = path_room_list[idx+1]
                room1_loc = path_room_list[idx]
                RoomFactory.connect_room(self.__room_list[room1_loc[0]][room1_loc[1]], self.__room_list[room2_loc[0]][room2_loc[1]],
                                         room1_loc, room2_loc)
            selected_room = random.sample(path_room_list[1:-1], 4)
            for room_idx in selected_room:
                pillar_room = self.__room_list[room_idx[0]][room_idx[1]]
                pillar_room.room_content = self.__pillar.pop(0)
            RoomFactory.update_room_as_exit(self.__room_list[curr_x][curr_y], curr_x, curr_y, self.__row_count - 1,
                                            self.__column_count - 1)

    def room_content_generator(self):
        """
        generate a sequence of random numbers based on the room has content
        """
        num = random.randint(0, sum(self.__room_content_count) + self.__empty_rooms)
        for idx in range(len(self.__room_content)):  # iterate through each room content type
            if num < self.__room_content_count[idx]:
                self.__room_content_count[idx] -= 1
                return list(self.__room_content.keys())[idx]
            else:
                num -= self.__room_content_count[idx]
        self.__empty_rooms -= 1
        return " "

    def cal_room_content(self):
        """
        Calculates the count of each room content type by percentage
        """
        self.__room_content_count = [math.floor(x * self.__empty_rooms) for x in self.__room_content.values()]
        self.__empty_rooms = self.__empty_rooms - sum(self.__room_content_count)

    def entrance_exit_pos(self):
        """"Gives other classes access to the private field of self.__entrance_exit_pos."""
        return self.__entrance_exit_pos

    def set_room_vision_potion(self):
        """
        Visualize the 8 adjacent rooms around the current room
        """
        for row, col in self.__vision_rooms:
            self.__room_list[row][col].vision_potion_rooms = self.get_vision_potion_rooms(row, col)

    def get_vision_potion_rooms(self, row, col):
        """
        Visualize the 8 adjacent rooms around the current room
        """
        rooms = []
        offsets = [-1, 0, 1]
        for r_offset in offsets:
            n_row = row + r_offset
            if 0 <= n_row < self.__row_count:
                room = []
                for c_offset in offsets:
                    n_col = col + c_offset
                    if 0 <= n_col < self.__column_count:
                        room.append(self.__room_list[n_row][n_col])
                rooms.append(room)
        return rooms

    def __str__(self):
        """
        Returns a str visualization of the dungeon.
        """
        res = ""
        for row in self.__room_list:
            for i in range(3):
                line = []
                for col in row:
                    line += col.room_matrix[i]
                    line.append(" ")
                res += "".join(line) + "\n"
        return res


if __name__ == "__main__":
    dungeon = Dungeon(6, 6)
    dungeon.dungeon_generator()
    print(dungeon)
    # print(dungeon.entrance_exit_generator())
    # print(dungeon.set_room_content())
