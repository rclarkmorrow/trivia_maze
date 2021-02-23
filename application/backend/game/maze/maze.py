class Maze:
    def __init__(self, row_count, col_count):
        self.__room_list = []  # Update this
        self.__row_count = row_count
        self.__col_count = col_count
        self.__entrance_exit_pos = [0, 0]  # Update this
        self.__empty_rooms = int
        # May not need this as it's being tracked in the
        # game state.
        self.__player_pos = None

    @property
    def room_list(self):
        return self.__room_list

    @property
    def entrance_pos(self):
        return self.__entrance_exit_pos[0]

    @property
    def exit_pos(self):
        return self.__entrance_exit_pos[1]

    @property
    def player_pos(self):
        return self.__player_pos