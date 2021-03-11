# Standard library imports
import sys
import math
import random
from pathlib import Path
from collections import deque
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append((str(package_root_directory)))
from game.room.room_factory import RoomFactory  # noqa


class Maze:
    """
      Class holds information about a grid of rooms and methods that
      determine whether the maze can be traversed from a given position
      to an exit.
      :param row_count: number of rows as int > 1
      :param col_count: number of columns as int > 1
    """
    def __init__(self, row_count: int, col_count: int):
        if row_count < 2:
            raise ValueError('Row count must be an integer greater than zero')
        if col_count < 2:
            raise ValueError('Col count must be an integer greater than zero')

        self.__row_count = row_count
        self.__col_count = col_count
        self.__grid = self.__maze_generator()  # 2D List of Room instances.
        # Entrance and exit are each a list of x, y indices.
        self.__entrance, self.__exit = self.__random_entrance_exit()

    @property
    def row_count(self):
        """ Returns row count as property. """
        return self.__row_count

    @property
    def col_count(self):
        """ Returns column count as property. """
        return self.__col_count

    @property
    def size(self):
        """ Returns grid size as property. """
        return self.__row_count * self.__col_count

    @property
    def grid(self):
        """ Returns room list as property. """
        return self.__grid

    @property
    def entrance(self):
        """ Returns maze entrance as property. """
        return self.__entrance

    @property
    def exit(self):
        """ Returns maze exit as property. """
        return self.__exit

    def can_reach_exit(self, position):
        """
          Returns whether the exit is reachable as bool property.
          :param position: List of x,y indices for current position
          :Return: True if exit is reachable, False if not
        """
        return self.__verify_exit_path(position)

    def __maze_generator(self):
        """
          Method generates a maze and sets the entrance point, exit point
          and fills cells with instances of Rooms
          :Return: 2D list of rooms
        """
        grid = []
        for row in range(self.__row_count):
            new_row = []
            for col in range(self.__col_count):
                new_row.append(RoomFactory.create_room([row, col]))
                if col > 0:
                    new_row[col].left = new_row[col - 1]
                    new_row[col - 1].right = new_row[col]
                if row > 0:
                    new_row[col].up = grid[row - 1][col]
                    grid[row - 1][col].down = new_row[col]
            grid.append(new_row)
        return grid

    def __get_random_indices(self):
        """ Returns random indices based on grid size. """
        rand_row = random.randint(0, self.__row_count - 1)
        rand_col = random.randint(0, self.__col_count - 1)
        return [rand_row, rand_col]

    def __random_entrance_exit(self):
        """ Returns random entrance and exit coordinates. """
        # Generate random entrance and exit coordinates.
        while True:
            get_random = False
            rand_entrance = self.__get_random_indices()
            rand_exit = self.__get_random_indices()
            # Entrance and exit coordinates must be different.
            if rand_entrance == rand_exit:
                get_random = True
            # Make sure there is some distance between entrance and exit.
            distance = (abs(rand_entrance[0] - rand_exit[0]) +
                        abs(rand_entrance[1] - rand_exit[1]))

            if distance < round(math.sqrt(self.size) - 1):
                get_random = True
            if not get_random:
                # Set rooms to entrance and exit and return
                self.__grid[rand_entrance[0]][rand_entrance[1]].is_entrance = True
                self.__grid[rand_exit[0]][rand_exit[1]].is_exit = True

                return rand_entrance, rand_exit

    def __can_enter(self, position, traversed):
        """ Determine if the room is able to be entered. """
        row, col = position
        # Check index values
        if row < 0 or col < 0:
            return False
        if row >= self.__row_count or col >= self.__col_count:
            return False
        # Check if already traversed
        if traversed[row][col]:
            return False
        # Check if blocked
        if self.__grid[row][col].blocked:
            return False
        return True

    def __verify_exit_path(self, position=None):
        """
          Method determines whether the exit to the maze can still be
          reached. Defaults to checking from the maze entrance.
          :param position: The coordinates to check traversal from
          :Returns: True if exit can be reached, False if it can't.
        """

        # Start from entrance if no position provided.
        if not position:
            position = self.__entrance

        # Create search queue, traversed list and return condition.
        search_queue = deque()
        search_queue.append(position)
        traversed = [[False for _ in range(self.__col_count)]
                     for _ in range(self.__row_count)]
        can_exit = False

        # Add first position to traversed
        row, col = position
        traversed[row][col] = True

        count = 0
        # Loop through the queue, adding new positions.
        while search_queue:
            # Grab first position.
            count += 1
            row, col = search_queue.popleft()
            # Check if room is exit.
            if [row, col] == self.__exit:
                can_exit = True
                break
            # Add positions to queue if valid.
            if (self.__grid[row][col].up and
                    self.__can_enter([row - 1, col], traversed)):
                search_queue.append([row - 1, col])
                traversed[row - 1][col] = True
            if (self.__grid[row][col].right and
                    self.__can_enter([row, col + 1], traversed)):
                search_queue.append([row, col + 1])
                traversed[row][col + 1] = True
            if (self.__grid[row][col].down and
                    self.__can_enter([row + 1, col], traversed)):
                search_queue.append([row + 1, col])
                traversed[row + 1][col] = True
            if (self.__grid[row][col].left and
                    self.__can_enter([row, col - 1], traversed)):
                search_queue.append([row, col - 1])
                traversed[row][col - 1] = True
        return can_exit
