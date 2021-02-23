import random
from Adventurer import Adventurer
from Dungeon import Dungeon


class DungeonAdventure:
    """
    This class contains the main logic for the Dungeon Adventure game.
    """
    @staticmethod
    def game_starter():
        """
        Introduces the player to the game. Creates an adventurer with the given name.
        Creates a dungeon of given dimensions. Allows the player to move and play the game.
        """
        print("Welcome to our Dungeon game!")
        name = str(input("What's your name? "))
        column_count = int(input("Please input an integer as the number of columns dungeon "))
        row_count = int(input("Please input an integer as the number of rows of the dungeon "))
        dungeon = Dungeon(column_count, row_count)
        dungeon.dungeon_generator()
        adventurer = Adventurer(name)
        hit_point = adventurer.hit_points
        pillar_collected = adventurer.pillar_collected
        healing_potion_count = adventurer.healing_potion_count
        vision_potion_count = adventurer.vision_potion_count
        curr_x, curr_y = dungeon.entrance_exit_pos()[0]
        exit_x, exit_y = dungeon.entrance_exit_pos()[1]
        dire_map = {"l": [0, -1], "r": [0, 1], "u": [-1, 0], "d": [1, 0]}

        while True:
            move = input("Where would you like to move next, please enter 'l' for left, 'r' for 'right', 'u' for 'up',"
                         " 'd' for 'down', 'e' for exit, 's' for showing the whole dungeon map")
            if move == "e":
                break
            if move == "s":
                print(dungeon)
            if move not in dire_map:
                print(f"Please input a valid string among {dire_map.keys()}, e , s")
                continue
            dire = dire_map[move]
            next_x = curr_x + dire[0]
            next_y = curr_y + dire[1]
            if DungeonAdventure.if_passable(dungeon, curr_x, curr_y, next_x, next_y, column_count, row_count):
                next_room = dungeon.room_list[next_x][next_y]
                curr_room = next_room
                if hit_point < 0:
                    print("You have lost all the hit points.")
                    break
                print(f"=============== current room content is {curr_room.room_content}===============")
                if curr_room.room_content == "X":
                    pit_point = random.randint(1, 20)
                    hit_point = hit_point - pit_point
                    curr_room.room_content = " "
                    print(f'Your current hit points are {hit_point}')
                elif curr_room.room_content == "H":
                    healing_point = random.randint(1, 40)
                    hit_point = hit_point + healing_point
                    print(f'Your current hit points are {hit_point}')
                    healing_potion_count += 1
                    curr_room.room_content = " "
                elif curr_room.room_content == "A" or curr_room.room_content == "E" or curr_room.room_content == "I" or \
                        curr_room.room_content == "P":
                    pillar_collected.append(curr_room.room_content)
                    curr_room.room_content = " "
                elif curr_room.room_content == "V":
                    vision_potion_count += 1
                    print(dungeon.get_vision_potion_rooms())
                adventurer.hit_points = hit_point
                curr_x, curr_y = next_x, next_y
                if (curr_x, curr_y) == (exit_x, exit_y):
                    print("Congratulations! You have reach the destination!")
                    break
                print(f"{name} is in ({curr_x}, {curr_y})")
                print(adventurer)
            else:
                print("You can't move in this direction")

    @staticmethod
    def if_passable(dungeon: Dungeon, curr_x: int, curr_y: int, next_x: int, next_y: int, column_count: int,
                    row_count: int):
        """
        Tests if next room is passable or not by looking up if the next room is out of dungeon boundary or the doors are
        paired
        """
        diff_x = next_x - curr_x
        diff_y = next_y - curr_y
        # key value pair of the direction and the doors need to be paired between two rooms
        direction = {(0, 1): [[1, 2], [1, 0]], (0, -1): [[1, 0], [1, 2]], (-1, 0): [[0, 1], [2, 1]],
                     (1, 0): [[2, 1], [0, 1]]}

        [row1, col1], [row2, col2] = direction[(diff_x, diff_y)]

        if 0 <= next_y <= column_count - 1 and 0 <= next_x <= row_count - 1:
            curr_room = dungeon.room_list[curr_x][curr_y]
            next_room = dungeon.room_list[next_x][next_y]
            if curr_room.room_matrix[row1][col1] == next_room.room_matrix[row2][col2] != "*":
                [row1, col1], [row2, col2] = direction[(diff_x, diff_y)]
            if curr_room.room_matrix[row1][col1] == next_room.room_matrix[row2][col2] != "*":
                return True
            else:
                print("Dead end. No enter.")
                return False
        else:
            print("You are moving out of the dungeon boundary.")
        return False


if __name__ == "__main__":
    DungeonAdventure.game_starter()
