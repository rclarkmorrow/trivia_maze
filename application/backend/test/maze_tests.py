import unittest
import sys
from pathlib import Path
# Setup local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.maze.maze import Maze  # noqa


class MazeTests(unittest.TestCase):
    """ Unit Tests for Maze class. """

    def test_create_maze(self):
        """ Test create maze. """
        maze = Maze(4, 4)

        self.assertEqual(maze.row_count, 4)
        self.assertEqual(maze.col_count, 4)
        self.assertEqual(maze.size, 16)
        self.assertTrue(isinstance(maze.entrance, list))
        self.assertTrue(isinstance(maze.exit, list))
        self.assertEqual(len(maze.entrance), 2)
        self.assertEqual(len(maze.exit), 2)
        for number in maze.entrance:
            self.assertTrue(isinstance(number, int))
        for number in maze.exit:
            self.assertTrue(isinstance(number, int))


if __name__ == '__main__':
    unittest.main()