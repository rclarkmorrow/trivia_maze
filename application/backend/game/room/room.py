class Room:
    def __init__(self, features):
        self.__features = features
        self.__visited = False  # Bool
        self.__blocked = False  # Bool

    @property
    def features(self):
        """ Returns features as property. """
        return self.__features

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
