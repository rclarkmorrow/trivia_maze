# System imports
import unittest
import sys
from pathlib import Path
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from game.trivia_maze_game import TriviaMazeGame  # noqa
from game.player.player import Player  # noqa
from game.maze.maze import Maze  # noqa
from database.question.question import Question  # noqa


class TriviaMazeGameTests(unittest.TestCase):
    """ Unit Tests for TriviaMazeGame class. """

    @staticmethod
    def create_questions(question_range=3, answer_range=3):
        """ Method creates a list of questions and answer in given range. """
        question_list = []
        # Create some questions to pass to game object.
        for question in range(question_range):
            flag_correct = True
            question = f'question number {question + 1}'
            answer_list = []
            for answer in range(answer_range):
                if flag_correct:
                    answer_list.append([f'answer number {answer + 1}', 1])
                    flag_correct = False
                else:
                    answer_list.append([f'answer number {answer + 1}', 0])
            question_list.append(Question(question, answer_list))
        return question_list

    def test_create_game(self):
        """ Test TriviaMazeGame created with appropriate properties. """

        questions = self.create_questions()
        game = TriviaMazeGame('Roger', 4, 4, questions)

        self.assertTrue(isinstance(game, TriviaMazeGame))
        self.assertTrue(isinstance(game.maze, Maze))
        self.assertTrue(isinstance(game.player, Player))
        self.assertEqual(game.player.name, 'Roger')
        self.assertTrue(game.maze.row_count == game.row_count == 4)
        self.assertTrue(game.maze.col_count == game.col_count == 4)
        for question in game.questions:
            self.assertTrue(isinstance(question, Question))
        self.assertEqual(game.questions[0].question, 'question number 1')
        self.assertEqual(game.questions[1].question, 'question number 2')
        self.assertEqual(game.questions[2].question, 'question number 3')
        for answer in range(3):
            if answer == 0:
                is_correct = 1
            else:
                is_correct = 0
            self.assertEqual(game.questions[0].answers[answer],
                             [f'answer number {answer + 1}', is_correct])
            self.assertEqual(game.questions[1].answers[answer],
                             [f'answer number {answer + 1}', is_correct])
            self.assertEqual(game.questions[2].answers[answer],
                             [f'answer number {answer + 1}', is_correct])
        self.assertEqual(game.current_question, None)
        self.assertTrue(len(game.entrance) == 2)
        self.assertTrue(len(game.exit) == 2)
        self.assertEqual(game.entrance, game.player_position)
        self.assertEqual(game.visited_rooms, [])
        self.assertEqual(game.blocked_rooms, [])
        self.assertEqual(game.cheat_mode, False)

    def test_set_player_position(self):
        """ Test TriviaMazeGame setting player position. """

        questions = self.create_questions()
        game = TriviaMazeGame('Roger', 4, 4, questions)
        game.player_position = [3, 3]

        self.assertEqual([3, 3], game.player_position)

        # TODO: create logic to confirm position is sent as list of ints
        #  and prevent a position greater than the size
        #  limits of the maze, and return ValueError if attempted

    def test_trivia_maze_question(self):
        """ Test TriviaMazeGame question returns question. """

        questions = self.create_questions(question_range=3, answer_range=4)
        game = TriviaMazeGame('Roger', 4, 4, questions)

        question = game.question

        self.assertTrue(isinstance(question, dict))
        # Question is popped from the end of the list (e.g. number 3)
        self.assertEqual(question['Question'], 'question number 3')

    def test_trivia_maze_question_none_when_empty(self):
        """ Test TriviaMazeGame question returns question. """

        questions = self.create_questions(question_range=3, answer_range=4)
        game = TriviaMazeGame('Roger', 4, 4, questions)

        for _ in range(len(game.questions)):
            _ = game.question

        question = game.question

        self.assertEqual(question, None)

    def test_toggle_cheat_mode_true(self):
        """ Test TriviaMazeGame question returns question. """

        questions = self.create_questions(question_range=3, answer_range=4)
        game = TriviaMazeGame('Roger', 4, 4, questions)

        game.cheat_mode = True

        self.assertEqual(True, game.cheat_mode)

    def test_toggle_cheat_mode_False(self):
        """ Test TriviaMazeGame question returns question. """

        questions = self.create_questions(question_range=3, answer_range=4)
        game = TriviaMazeGame('Roger', 4, 4, questions)

        game.cheat_mode = True
        game.cheat_mode = False

        self.assertEqual(False, game.cheat_mode)


if __name__ == '__main__':
    unittest.main()
