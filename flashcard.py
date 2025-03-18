class flashcard:
    '''allows us to flip the card, with values being the front, back'''
    def __init__(self, question, answer):
        self.question=question
        self.answer=answer
        self.side_up="question side"