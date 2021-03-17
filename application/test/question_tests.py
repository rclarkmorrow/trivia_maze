import unittest
import sys
from pathlib import Path
# Setup local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from database.question.question import Question  # noqa


class QuestionTests(unittest.TestCase):
    """ Unit Tests for Question class. """

    def test_create_question(self):
        """ Test can create question with properties. """

        description = 'What is your quest?'
        answers = [
            ['Green, no blue', 0],
            ['To seek the holy grail.', 1],
            ['I don\'t know that', 0],
            ['African or English swallow?', 0]
        ]
        question = Question(description, answers)

        self.assertTrue(isinstance(question, Question))
        self.assertEqual(question.question, description)
        self.assertEqual(question.answers, answers)

    def test_create_question_non_string(self):
        """
        Test TypeError when creating question with non-string question.
        """
        description = 501
        answers = [
            ['Green, no blue', 0],
            ['To seek the holy grail.', 1],
            ['I don\'t know that', 0],
            ['African or English swallow?', 0]
        ]
        try:
            _ = Question(description, answers)
            self.assertEqual(True, False, 'Should not have got here: question'
                                          ' created with non strong question.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_question_answer_non_list(self):
        """ Test TypeError when creating question with non-list answer. """
        description = 'What is your quest?'
        answers = ['I am not a list', 2]
        try:
            _ = Question(description, answers)
            self.assertEqual(True, False, 'Should not have got here: question'
                                          ' created with a  non list answer.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_question_answer_non_string(self):
        """ Test TypeError when creating question with non-string answer. """
        description = 'What is your quest?'
        answers =         answers = [
            ['Green, no blue', 0],
            [2, 1],
            ['I don\'t know that', 0],
            ['African or English swallow?', 0]
        ]
        try:
            _ = Question(description, answers)
            self.assertEqual(True, False, 'Should not have got here: question'
                                          ' created with non string answer.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_question_answer_non_binary(self):
        """ Test TypeError when creating question with non-string answer. """
        description = 'What is your quest?'
        answers = [
            ['Green, no blue', 5],
            ['To seek the holy grail.', 1],
            ['I don\'t know that', 0],
            ['African or English swallow?', 0]
        ]
        try:
            _ = Question(description, answers)
            self.assertEqual(True, False, 'Should not have got here: question'
                                          ' created with non binary answer'
                                          ' flag.')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_question_valid_formatted(self):
        """ Test to make sure formatted answer returns correctly. """
        description = 'What is your quest?'
        answers = [
            ['Green, no blue', 0],
            ['To seek the holy grail.', 1],
            ['I don\'t know that', 0],
            ['African or English swallow?', 0]
        ]
        question = Question(description, answers)
        question_format = question.formatted

        self.assertTrue(isinstance(question_format, dict))
        self.assertEqual(question.question,
                         question_format['Question'])
        for answer in question.answers:
            if answer[1] == 1:
                check = False
                for correct_answer in question_format['Correct']:
                    if answer[0] == question_format['Answers'][correct_answer]:
                        check = True
                self.assertTrue(check)
            self.assertTrue(answer[0] in question_format['Answers'].values())


if __name__ == '__main__':
    unittest.main()
