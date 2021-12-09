def visualize_basins(basins, length_x, length_y):
    for b in basins:
        print("BASIN:", b)
        print(f"Basin size is {len(b)}")
        for y in range(length_y):
            row = ""
            for x in range(length_x):
                found = False
                for element in b:
                    if y == element[0] and x == element[1]:
                        row += " " + str(element[2]) + " "
                        found = True
                if not found:
                    row += " . "
            print(row)
