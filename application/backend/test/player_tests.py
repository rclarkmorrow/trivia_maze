import unittest
import sys
from pathlib import Path
# Setup local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.player.player_factory import PlayerFactory, DEFAULT_NAMES  # noqa
from game.player.player import Player  # noqa


class PlayerTests(unittest.TestCase):
    """ Unit Tests for Player and Player classes. """

    """"-------------------------------------------------- #
    #  PLAYER FACTORY TESTS                                #
    #----------------------------------------------------"""

    def test_create_player_no_name(self):
        """ Player factory creates player with no name. """
        player = PlayerFactory.create_player()

        self.assertTrue(player.name in DEFAULT_NAMES)
        self.assertEqual(0, player.points)
        self.assertEqual([], player.inventory)

    def test_create_player_name(self):
        """ Player factory creates player with name. """
        player = PlayerFactory.create_player(name='Dennis')

        self.assertEqual('Dennis', player.name)
        self.assertEqual(0, player.points)
        self.assertEqual([], player.inventory)

    def test_create_player_name_not_string(self):
        """ TypeError when player factory creates player
        with non-string name. """
        try:
            _ = PlayerFactory.create_player(name=4.0)
            self.assertEqual(True, False, 'should not have got here:'
                                          ' player created with name not'
                                          ' of type int.')
        except TypeError:
            self.assertEqual(True, True)

    """"-------------------------------------------------- #
    #  PLAYER TESTS                                        #
    #----------------------------------------------------"""

    def test_player_created_with_name(self):
        """ Player created with name. """
        player = Player('Dennis')

        self.assertEqual('Dennis', player.name)

    def test_player_created_no_name(self):
        """ TypeError when player created with no name. """
        try:
            _ = Player()
            self.assertEqual(True, False, 'should not have got here: player'
                                          ' created with no name.')
        except TypeError:
            self.assertEqual(True, True)

    def test_player_created_with_zero_points(self):
        """ Player is created with no points. """
        player = Player('Dennis')

        self.assertEqual(0, player.points)

    def test_player_created_with_empty_inventory(self):
        """ Player is created with no inventory (empty list). """
        player = Player('Dennis')

        self.assertEqual([], player.inventory)

    def test_player_adjust_points_positive(self):
        """ Can add points to player. """
        player = Player('Dennis')
        player.adjust_points(10)

        self.assertEqual(10, player.points)

    def test_player_adjust_points_negative(self):
        """ Can remove points from player. """
        player = Player('Dennis')
        player.adjust_points(100)
        player.adjust_points(-10)

        self.assertEqual(90, player.points)

    def test_player_adjust_points_below_zero(self):
        """ Player points can't go below zero. """
        player = Player('Dennis')
        player.adjust_points(-10)

        self.assertEqual(0, player.points)

    def test_player_add_item(self):
        """ Can add to player inventory. """
        player = Player('Dennis')
        player.add_item('i am an item.')

        self.assertEqual(['i am an item.'], player.inventory)

    def test_player_remove_item(self):
        """ Can add to player inventory. """
        player = Player('Dennis')
        for item in range (3):
            player.add_item(f'i am item {item}.')
        player.remove_item('i am item 1.')

        self.assertEqual(['i am item 0.', 'i am item 2.'], player.inventory)


if __name__ == '__main__':
    unittest.main()
