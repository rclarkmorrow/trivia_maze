# Standard library imports
from collections import deque
from random import sample
from math import sqrt
# Local package imports
from game.room.room_factory import RoomFactory


class Maze:
    """
      Class holds information about a grid of rooms and methods that
      determine whether the
    """
    def __init__(self, row_count: int, col_count: int):
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

    def reach_exit(self, position):
        """
          Returns whether the exit is reachable as bool property.
          :param position: List of x,y indices for current position
          :Return: True if exit is reachable, False if not
        """
        return self.__reach_exit(position)

    def __maze_generator(self):
        """
          Method generates a maze and sets the entrance point, exit point
          and fills cells with instances of Rooms
          :Return: 2D list of rooms
        """
        grid = []
        for row in range(self.__row_count):
            row_rooms = []
            for col in range(self.__col_count):
                row_rooms.append(RoomFactory.create_room())
            grid.append(row_rooms)
        return grid

    def __random_entrance_exit(self):
        """ Returns random entrance and exit coordinates. """
        # Generate random entrance and exit coordinates.
        rand_entrance = sample(range(0, self.size - 1), 2)
        rand_exit = sample(range(0, self.size - 1), 2)
        # Entrance and exit coordinates must be different.
        if rand_entrance == rand_exit:
            self.__random_entrance_exit()
        # Make sure there is some distance between entrance and exit.
        distance = (abs(rand_entrance[0] - rand_exit[0]) +
                    abs(rand_entrance[1] - rand_exit[1]))
        if distance < round(sqrt(self.size) - 1):
            self.__random_entrance_exit()

        return rand_entrance, rand_exit

    def __can_enter(self, position, visited=[]):
        """ Determine if the room is able to be entered. """
        row, col = position
        # If room has been visited in search, is out of index
        # range or is blocked, return false. Otherwise return
        # True.
        if position in visited:
            return False
        if row < 0 or col < 0:
            return False
        if row >= self.__row_count or col >= self.__col_count:
            return False
        if self.__grid[row][col].blocked:
            return False
        return True

    def __reach_exit(self, position=None):
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
        visited = []
        can_exit = False
        # Loop through the queue, adding new positions.
        while search_queue:
            # Grab first position.
            row, col = search_queue.popleft()
            # Check if room is exit.
            if [row, col] == self.__exit:
                can_exit = True
            visited.append([row, col])
            # Add valid surrounding rooms to search_queue: north/up
            # east/right, south/down, west/left.
            if self.__can_enter([row - 1, col], visited):
                search_queue.append([row - 1, col])
            if self.__can_enter([row, col + 1], visited):
                search_queue.append([row, col + 1],)
            if self.__can_enter([row + 1, col], visited):
                search_queue.append([row + 1, col],)
            if self.__can_enter([row, col - 1], visited):
                search_queue.append ([row, col - 1],)

        return can_exit
