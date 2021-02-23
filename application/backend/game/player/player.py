class Player:
    """
      Player class holds information about the player
      of a trivia maze game. For now it covers information
      related to a single game, but could have other details
      added and be written to a database to persist data
      over multiple sessions. A cumulative score, for example.
      :param: name (takes the name of the player, and creates
              player instance with that name.
    """
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__inventory = []

    @property
    def name(self):
        """ Returns name as property. """
        return self.__name

    @property
    def points(self):
        """ Returns points as property. """
        return self.__points

    @property
    def inventory(self):
        """ Returns inventory as property. """
        return self.__inventory

    def adjust_points(self, points):
        """
          Adjusts points to the player's point total
          based on the parameter provided to a minimum
          of zero points.
          :param: points (the number of points to adjust the
                  player's point total by -- can be a positive
                  or negative integer).
        """
        # Points equals the greater of the sum or zero.
        self.__points = max(self.__points + points, 0)

    def remove_item(self, item):
        """
          Removes and item from the player's inventory.
          :param: item (the item to remove from the
                  player's inventory.)
          :return success: if the item is successfully removed from
                           the player's inventory, returns True with
                           a success message.
          :return failure: if the item is not in the player's
                           inventory, returns False with an error
                           message
        """
        try:
            self.__inventory.remove(item)
            return True, f'{item} removed.'
        except ValueError as error:
            return False, error

    def add_item(self, item):
        """
          Adds an item to the player's inventory.
          :param: item (the item to be added to the player's
                  inventory.
        """
        self.__inventory.append(item)
