import sqlite3
from sqlite3 import Error


class TriviaMazeDB:

    @staticmethod
    def create_connection():
        my_conn = None
        try:
            my_conn = sqlite3.connect("TriviaDB.db")
        except Error as e:
            print(e)
        return my_conn

    @staticmethod
    def select_question_answers(db_connection, question_no):
        try:
            if 0 < question_no <= 40:
                cur = db_connection.cursor()
                sql = ''' SELECT
                          q.Description as question
                          ,a.description as answer
                          ,a.isCorrect
                          FROM Questions as q 
                          LEFT JOIN Answers as a ON q.Question_ID = a.Question_ID 
                          WHERE q.Question_ID = ?
                     '''
                cur.execute(sql, (question_no,))
                my_records = cur.fetchall()
                cur.close()

                return my_records

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")


if __name__ == "__main__":
    db = TriviaMazeDB
    conn = db.create_connection()
    records = db.select_question_answers(conn, 1)
    for row in records:
        print("Question :", row[0])
        print("Answer :", row[1])
        print("IsCorrect :", row[2])