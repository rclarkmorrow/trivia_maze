from game.room.room import Room


class RoomFactory:
    """
     This class creates instances of a room object.
    """

    @staticmethod
    def create_room(features=[]):
        return Room(features)
