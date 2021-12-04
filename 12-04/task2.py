import csv
from Board import Board

# Parse bingo board data
with open("boards.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    # read and clean entries
    board_data = [[int(y) for y in x if y != ''] for x in list(reader)]

# cut board data into individual boards
boards = []
for i in range(int(len(board_data) / 6)):
    index_start = (i * 6) + 1
    index_end = (i * 6) + 6
    boards.append(Board(board_data[index_start:index_end]))

# parse bingo numbers
with open("numbers.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    numbers = [int(x) for x in list(reader)[0]]

# play bingo -> look for last winner (wait for his winning number to appear!)
winner = None
remaining_boards = boards
for n in numbers:
    for b in boards[:]:
        b.mark_number(n)
        if b.check_winning_conditions():
            if len(boards) == 1:
                winner = boards[0]
                winning_number = n
                break
            else:
                boards.remove(b)
    if winner is not None:
        break

score = winner.calculate_score()
print(winner)
print("score", score)
print("winning_number", winning_number)
print("Result:", score * winning_number)
