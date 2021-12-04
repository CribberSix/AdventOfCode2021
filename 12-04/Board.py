class Board:

    def __init__(self, data):
        self.rows = data
        self.marked = [[0 for _ in range(0, 5)] for _ in range(0, 5)]

    def __str__(self):
        """String representation"""
        res = "BOARD:"
        for r in self.rows:
            res = res + "\n" + str(r)
        res = res + "\nMARKED:"
        for r in self.marked:
            res = res + "\n" + str(r)
        return res

    def mark_number(self, number:int) -> None :
        """
        Marks a number in the bingo board.

        :param number: Number to be looked up in the board's numbers.
        :return: None
        """
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                if cell == number:
                    self.marked[i][j] = 1

    def check_winning_conditions(self) -> bool:
        """
        Checks whether a winning condition (5x "1" in a row or a columN) is fulfilled in the board.

        :return: Boolean, signifying win/loss
        """
        for row in self.marked:  # sum rows
            if sum(row) == 5:
                return True
        for i in range(0, 5):  # sum columns
            if sum([x[i] for x in self.marked]) == 5:
                return True
        return False

    def calculate_score(self) -> int:
        """
        Calculates sum of unmarked cells.
        :return: score
        """
        score = 0
        for i, row in enumerate(self.marked):
            for j, cell in enumerate(row):
                if cell == 0:  # sum unmarked
                    score += self.rows[i][j]
        return score
