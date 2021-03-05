class Room:
    """
      This class
    """
    def __init__(self, position, features):
        self.__position = position  # List of x, y vertices or None
        self.__features = features  # List of room features or None
        self.__is_entrance = False  # Boolean.
        self.__is_exit = False  # Boolean.
        self.__up = None  # None or room instance.
        self.__right = None  # None or room instance.
        self.__down = None  # None or room instance.
        self.__left = None  # None or room instance.
        self.__visited = False  # Boolean.
        self.__blocked = False  # Boolean.

    @property
    def position(self):
        """ Returns position as a property. """
        return self.__position

    @property
    def features(self):
        """ Returns features as property. """
        return self.__features

    @property
    def is_entrance(self):
        """ Return is entrance as property. """
        return self.__is_entrance

    @is_entrance.setter
    def is_entrance(self, toggle: bool):
        """
          Sets flag to indicate whether room is an entrance.
          :param toggle: Boolean
        """
        self.__is_entrance = toggle

    @property
    def is_exit(self):
        """ Returns is exit as property. """
        return self.__is_exit

    @is_exit.setter
    def is_exit(self, toggle: bool):
        """
          Sets flag to indicate whether room is an exit.
          :param toggle: Boolean
        """
        self.__is_exit = toggle

    @property
    def up(self):
        """ Returns right (None or Room) as property. """
        return self.__up

    @up.setter
    def up(self, room):
        """
          Sets up room link.
          :param room: None or Room instance.
        """
        if room and type(room) != Room:
            raise TypeError('Type must be Room instance or None.')
        self.__up = room

    @property
    def right(self):
        """ Returns right (None or Room) as property. """
        return self.__right

    @right.setter
    def right(self, room):
        """
          Sets right room link.
          :param room: None or Room instance.
        """
        if room and type(room) != Room:
            raise TypeError('Type must be Room instance or None.')
        self.__right = room

    @property
    def down(self):
        """ Returns down (None or Room) as property. """
        return self.__down

    @down.setter
    def down(self, room):
        """
          Sets down room link.
          :param room: None or Room instance.
        """
        if room and type(room) != Room:
            raise TypeError('Type must be Room instance or None.')
        self.__down = room

    @property
    def left(self):
        """ Returns left (None or Room) as property. """
        return self.__left

    @left.setter
    def left(self, room):
        """
          Sets left room link.
          :param room: None or Room instance.
        """
        if room and type(room) != Room:
            raise TypeError('Type must be Room instance or None.')
        self.__left = room

    @property
    def visited(self):
        """ Returns visited as property. """
        return self.__visited

    @visited.setter
    def visited(self, toggle: bool):
        """ Sets the visited status for a room. """
        self.__visited = toggle

    @property
    def blocked(self):
        """ Returns blocked as property. """
        return self.__blocked

    @blocked.setter
    def blocked(self, toggle: bool):
        """ Sets the blocked status for a room. """
        self.__blocked = toggle

    def add_feature(self, feature):
        """ Adds new features to the room's feature list. """
        self.__features.append(feature)

    def remove_feature(self, feature):
        """ Removes a feature from a room's feature list. """
        self.__features.remove(feature)

    def draw_room(self):
        """
          Method returns an ASCII representation of the room.
          :Return: Tuple containing top, middle, and bottom strings
                   representing the room.
        """
        if self.__up:
            top = '*———*'
        else:
            top = '*****'
        if self.__left:
            middle = '|'
        else:
            middle = '*'
        if self.__is_entrance:
            middle += 'N'
        elif self.__is_exit:
            middle += 'X'
        elif self.__features:
            middle += ' F '
        else:
            middle += '   '
        if self.__right:
            middle += '|'
        else:
            middle += '*'
        if self.__down:
            bottom = '*———*'
        else:
            bottom = '*****'

        return top, middle, bottom

    def __str__(self):
        """
          Returns a string of human readable details about
          a room instance.
        """
        return (
            f'Position: {self.__position}\n'
            f'Features? {True if self.__features else False}\n'
            f'Entrance? {self.__is_entrance}\n'
            f'Exit? {self.__is_exit}\n'
            f'Visited? {self.__visited}\n'
            f'Blocked? {self.__blocked}\n'
            '-- Exits --\n'
            f'Up: {True if self.__up else False}\n'
            f'Right: {True if self.__right else False}\n'
            f'Down: {True if self.__down else False}\n'
            f'Left: {True if self.__left else False}\n'
            '-- Entrances --\n'
            f'Up: {True if self.__up and self.__up.down else False}\n'
            f'Right: {True if self.__right and self.__right.left else False}\n'
            f'Down: {True if self.__down and self.__down.up else False}\n'
            f'Left: {True if self.__left and self.__left.right else False}\n'
        )
