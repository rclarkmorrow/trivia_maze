import random


class Adventurer:
    """
    The Adventurer is a player of the Dungeon Adventure game.
    An Adventurer has a given name, amount of points, counts of potions collected, and list of pillars collected.
    """
    
    def __init__(self, name):
        """
        Adventurer constructor to start with setting the players name, 
        random amount of points between 75 and 100 points,
        no healing potions, vision potions, or pillars collected.
        """
        self.__name = name
        self.__hit_points = random.randint(75, 100)
        self.__healing_potion = 0
        self.__vision_potion = 0
        self.__pillar_collected = []

    @property
    def hit_points(self):
        """"Gives other classes access to the private field of self.__hit_points."""
        return self.__hit_points

    @hit_points.setter
    def hit_points(self, point_change: int):
        """Allows other classes to modify the value of self.__hit_points as the game is played."""
        self.__hit_points = point_change

    @property
    def healing_potion_count(self):
        """"Gives other classes access to the private field of self.__healing_potion."""
        return self.__healing_potion

    @healing_potion_count.setter
    def healing_potion_count(self, healing_potion: int):
        """Allows other classes to modify the value of self.__healing_potion as the game is played."""
        self.__healing_potion = healing_potion

    @property
    def vision_potion_count(self):
        """"Gives other classes access to the private field of self.__vision_potion."""
        return self.__vision_potion

    @vision_potion_count.setter
    def vision_potion_count(self, vision_potion: int):
        """Allows other classes to modify the value of self.__vision_potion as the game is played."""
        self.__vision_potion = vision_potion

    @property
    def pillar_collected(self):
        """"Gives other classes access to the private field of self.__pillar_collected."""
        return self.__pillar_collected

    def __str__(self):
        """Returns the Adventurer's information as a string."""
        return f'Name {self.__name}, \nTotal Hit Points = {self.__hit_points}, \nTotal Healing Potion = ' \
               f'{self.__healing_potion}, \nTotal Vision Potion' \
               f' = {self.__vision_potion}, \nList of Pillars Pieces Found = {self.__pillar_collected}'


if __name__ == "__main__":
    adv = Adventurer("tututu")
    print(adv)


