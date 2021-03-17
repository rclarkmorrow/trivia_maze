import unittest
import sys
import random
from pathlib import Path
# Setup local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.maze.maze import Maze  # noqa


class MazeTests(unittest.TestCase):
    """ Unit Tests for Maze class. """

    def test_create_maze(self):
        """ Test create maze with properties. """
        maze = Maze(4, 4)
        self.assertEqual(maze.row_count, 4)
        self.assertEqual(maze.col_count, 4)
        self.assertEqual(maze.size, 16)
        self.assertTrue(isinstance(maze.entrance, list))
        self.assertTrue(isinstance(maze.exit, list))

    def test_create_maze_with_row_less_than_two(self):
        try:
            _ = Maze (1, 3)
            self.assertEqual(True, False, 'should not have got here: '
                                          'maze created with row < 2.')
        except ValueError:
            self.assertEqual(True, True)

    def test_create_maze_with_col_less_than_two(self):
        try:
            _ = Maze (3, 1)
            self.assertEqual(True, False, 'should not have got here: '
                                          'maze created with column < 2.')
        except ValueError:
            self.assertEqual(True, True)

    def test_create_maze_non_integer(self):
        """ Test create maze gets type error with non-integer. """
        try:
            _ = Maze('I am not an integer', 4)
            self.assertEqual(True, False, 'should not have got here: '
                             'maze created with non-integer index.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_maze_with_float(self):
        """ Test create maze gets type error with float. """
        try:
            _ = Maze(4.0, 4)
            self.assertEqual(True, False, 'should not have got here: '
                             'maze created with float index.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_entrance_is_list(self):
        """ Test maze creates entrance as list of two integers. """
        maze = Maze(4, 4)
        self.assertTrue(isinstance(maze.entrance[0], int))
        self.assertTrue(isinstance(maze.entrance[1], int))

    def test_create_entrance_is_list(self):
        """ Test mazes creates exit as list of two integers """
        maze = Maze(4, 4)
        self.assertTrue(isinstance(maze.exit[0], int))
        self.assertTrue(isinstance(maze.exit[1], int))

    def test_get_random_indices_in_range(self):
        """ Test maze creates random indices between 0 and len(row) and
        0 and len(column). """
        maze = Maze(10, 10)

        for test in range(1000):
            position = maze._Maze__get_random_indices()
            self.assertTrue(-1 < position[0] < 10)
            self.assertTrue(-1 < position[1] < 10)

    def test_indices_distance(self):
        """ Test maze creates random entrance and exit with enough
        distance between them. 10 x 10 maze, distance should never
        be less than 9. """
        maze = Maze(10, 10)

        for test in range(1000):
            self.assertTrue(
                (abs(maze.entrance[0] - maze.exit[0]) +
                abs(maze.entrance[1] - maze.exit[1])) >= 9)

    def test_maze_created_can_be_traversed(self):
        """ Test that a maze exit can be can be found at creation using
        private method __verify_exit_path. """
        maze = Maze(100, 100)

        self.assertTrue(maze._Maze__verify_exit_path())

    def test_maze_created_traversed_from_indices(self):
        """ Test that a maze exit can be found at creation
        from random positions. """
        maze = Maze(100, 100)

        for test in range(20):
            self.assertTrue(maze.can_reach_exit([random.randint(0, 99),
                                                 random.randint(0, 99)]))

    def test_maze_entrance_pointers_are_none(self):
        """ Test that maze can not be exited when entrance pointers are
        set to None. """
        maze = Maze(100, 100)

        row, col = maze.entrance
        maze.grid[row][col].up = None
        maze.grid[row][col].right = None
        maze.grid[row][col].down = None
        maze.grid[row][col].left = None

        self.assertFalse(maze.can_reach_exit([row, col]))

    def test_maze_exit_pointers_are_none(self):
        """ Test that a maze cannot be exited when rooms adjacent to the
        exit have their pointers set to None. """
        maze = Maze(100, 100)

        row, col = maze.exit
        if maze.grid[row][col].up:
            maze.grid[row][col].up.down = None
        if maze.grid[row][col].right:
            maze.grid[row][col].right.left = None
        if maze.grid[row][col].down:
            maze.grid[row][col].down.up = None
        if maze.grid[row][col].left:
            maze.grid[row][col].left.right = None

        self.assertFalse(maze.can_reach_exit([maze.entrance[0],
                                              maze.entrance[1]]))

    def test_maze_entrance_adjacent_are_blocked(self):
        """ Test that a maze cannot be exited when rooms adjacent to the
        entrance are blocked. """
        maze = Maze(100, 100)

        row, col = maze.entrance
        if row - 1 >= 0:
            maze.grid[row - 1][col].blocked = True
        if col + 1 < 100:
            maze.grid[row][col + 1].blocked = True
        if row + 1 < 100:
            maze.grid[row + 1][col].blocked = True
        if col - 1 >= 0:
            maze.grid[row][col - 1].blocked = True

        self.assertFalse(maze.can_reach_exit([row, col]))

    def test_maze_exit_adjacent_are_blocked(self):
        """ Test that a maze cannot be exited when rooms adjacent to the
        exit are blocked. """
        maze = Maze(100, 100)

        row, col = maze.exit
        if row - 1 >= 0:
            maze.grid[row - 1][col].blocked = True
        if col + 1 < 100:
            maze.grid[row][col + 1].blocked = True
        if row + 1 < 100:
            maze.grid[row + 1][col].blocked = True
        if col - 1 >= 0:
            maze.grid[row][col - 1].blocked = True

        self.assertFalse(maze.can_reach_exit([maze.entrance[0],
                                              maze.entrance[1]]))


if __name__ == '__main__':
    unittest.main()