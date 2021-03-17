import sqlite3
import sys
from pathlib import Path
from sqlite3 import Error
# Local imports
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append((str(package_root_directory)))
from database.question.question import Question  # noqa


class TriviaMazeDB:

    @staticmethod
    def create_connection():
        """ create a database connection to the SQLite database
            :param:
            :return: Connection object or None
        """
        my_conn = None
        try:
            my_conn = sqlite3.connect("./database/TriviaDB.db")
        except Error as e:
            print(e)
        return my_conn

    @staticmethod
    def __get_random(limit):
        """
          Method gets a random selection of questions from the trivia
          question database and returns them as a list of tuples.
          :param: db_connection
                  the database connection to use
          :param: limit
                  the maximum number of questions to return
        """

        db_connection = TriviaMazeDB.create_connection()
        try:
            cur = db_connection.cursor()

            # Query language that grabs question description (the question)
            # answer description (the answer) and is correct (boolean where
            # 0 is a false answer and 1 is a correct answer) and limits the
            # query results to a random selection of unique questions.
            sql = ''' SELECT 
                      q.Description,
                      a.Description,
                      a.isCorrect
                      FROM 
                      Questions as q,
                      Answers as a
                      WHERE q.Question_ID = a.Question_ID AND 
                      q.Question_ID IN (
                      SELECT
                      q.Question_ID 
                      FROM 
                      Questions as q
                      ORDER BY random()
                      LIMIT ?
                      )
            '''

            cur.execute(sql, (limit,))
            my_records = cur.fetchall()
            cur.close()

            return my_records

        except sqlite3.Error as error:
            return False, f'Failed to read data from sqlite table, {error}'

        finally:
            if cur:
                cur.close()

    @staticmethod
    def get_question_list(question_count):
        """
          Method creates a list of Question instances of a specified
          amount from a list of questions returned by a database call.
        """
        question_list = []
        results = TriviaMazeDB.__get_random(question_count)
        # Format question variables.
        current_question = results[0][0]
        answer_list = []

        # Loop through tuples in list of questions with a counter
        # starting at 1..
        for count, question in enumerate(results, 1):
            # While the question is the same, append the answer list
            # with a list of the answer and the boolean of whether it's
            # correct.
            if question[0] == current_question:
                answer_list.append([question[1], question[2]])
            # When the question changes, create a Question instance and
            # append it to the list, and reset the question variables.
            if question[0] != current_question:
                question_list.append(Question(current_question, answer_list))
                current_question = question[0]
                answer_list = [[question[1], question[2]]]
            # When the end of the list is reached, create a Question
            # instance and append it to the list.
            if count == len(results):
                question_list.append(Question(current_question, answer_list))

        # Return the list of Question instances.
        return question_list


if __name__ == "__main__":
    # Simple smoke test to verify that a list of Question instances
    # are returned and are correct.
    db = TriviaMazeDB
    conn = db.create_connection()
    questions = db.get_question_list(3)
    print(f'TYPE {type(questions)}')
    print(f'LENGTH {len(questions)}')
    print(f'QUESTIONS {questions},\n\n')
    for question in questions:
        print('*********QUESTION**************\n')
        print(f'Object type: {type(question)}\n')
        print(f'Object string:\n{question}\n')
        print(f'Question.formatted: {question.formatted}\n')
        print('*******************************\n\n')
