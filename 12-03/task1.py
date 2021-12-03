import csv

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    data = [x[0] for x in list(reader)]


def calculate_rate(_data, count_common):
    bitsequence = ""
    for i in range(0, len(_data[0])):
        # iterate over columns & get all values
        bits = [x[i] for x in _data]
        # determine which value is exists more often in the "column" & append to the sequence
        if bits.count("1") >= bits.count("0"):
            bitsequence = bitsequence + ("1" if count_common else "0")
        else:
            bitsequence = bitsequence + ("0" if count_common else "1")

    return bitsequence, int(bitsequence, 2)


_, b_gamma = calculate_rate(data, True)
_, b_epsilon = calculate_rate(data, False)
print(b_gamma * b_epsilon)  # 3901196

