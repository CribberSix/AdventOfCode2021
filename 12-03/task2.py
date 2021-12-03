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


def calculate_ox(_data, count_common):
    for i in range(len(_data[0])):
        # re-calculate with the reduced rows after every loop
        most_common_bits, _ = calculate_rate(_data, count_common)
        # filter rows to rows with the most common bit
        keep_rows = [row for row in _data if row[i] == most_common_bits[i]]
        if len(keep_rows) > 1:
            # start new cycle with the next column
            _data = keep_rows
        else:
            return keep_rows[0]


ox = calculate_ox(data, True)
print("ox:", ox, int(ox, 2))
co2 = calculate_ox(data, False)
print("c02:", co2, int(co2, 2))

print(int(ox, 2) * int(co2, 2))


