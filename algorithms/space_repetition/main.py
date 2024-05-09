class Card:
    reviewed_at = None
    next_review_at = None
    easiness = None
    interval = None
    repetitions = None

class SpaceRepetition:
    algo = None
    def calculate_next_review_date(self, card: Card):
        # use sm-2 algorithm to calculate next review date
        pass