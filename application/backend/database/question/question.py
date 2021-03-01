from random import sample

class Question:
    """
      The question class is a data structure for questions in the trivia
      maze game. It takes two parameters and creates a formatted dictionary
      that can be serialized in JSON and sent to a front-end client.
      :param: question
              a string that is the trivia question being asked
      :param: answers
              a list of lists formated as [an answer in string format, boolean
              indicating whether that answer is correct or not]
    """

    def __init__(self, question, answers):
        self.__question = question
        self.__answers = answers
        self.__formatted = self.__format_question()

    @property
    def question(self):
        """ Returns question as property."""
        return self.__question

    @property
    def answers(self):
        """ Returns answers as property. """
        return self.__answers

    @property
    def formatted(self):
        """ Returns formatted as property. """
        return self.__formatted

    def __str__(self):
        """ String representation of the question and answers """
        question_string = self.__question
        for answer in self.__answers:
            question_string += f'\n{answer[0]}: {answer[1]}'
        return question_string

    def __format_question(self):
        """
          Builds a dictionary representation of the question and its
          answers.
        """

        question_dictionary = {
            'Question': self.__question,
            'Answers': {},
            'Correct': [],
        }
        # Create dictionary entries for each answer where the key will be
        # alphabetical starting at lower case 'a' and append the list of
        # correct answers with the character key of a correct answer.
        for count, answer in enumerate(sample(self.__answers,
                                              len(self.__answers)), 97):
            question_dictionary['Answers'][chr(count)] = answer[0]
            if answer[1] == 1:
                question_dictionary['Correct'].append(chr(count))

        return question_dictionary


if __name__ == '__main__':
    # Basic smoke test confirms a question can be created and that the
    # order of answers are randomized.
    question = 'What is your quest?'
    answers = [['Green, no blue', 0], ['To seek the holy grail.', 1],
               ['I don\'t know that', 0], ['African or English swallow?', 0]]
    for i in range(1, 5):
        print(f'Loop {i}')
        format_question = Question(question, answers)
        print(f'fomated: {format_question.formatted}')
        print('\n\n')