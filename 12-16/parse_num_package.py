def parse_num_package(body: str) -> (str, int):
    """Parses a single package representing a decimal number.

    The binary string is padded with leading zeroes until length is a multiple of five bits.

    Each group of five bits start either with 1 or 0.  -> the one starting with 0 is the last group in the package!
    The four bits after the starting bit are used to describe the number. The function parses all groups, combines
    the resulting bit-strings and translates it into a decimal number.

    :param body: binary string representing the package contents.
    :returns: Tuple(str, int)
        str: the remaining binary string (e.g. the next packages).
        int: the decimal number of the current package.
    """
    i = 1
    nums = []
    current_nums = ''
    last_group = False
    for index, char in enumerate(body):
        if i == 1 and char == '0':
            nums.append(current_nums)  # add the previous group to the list
            current_nums = ''
            last_group = True
        elif i == 1 and char == '1':
            nums.append(current_nums)  # add the previous group to the list
            current_nums = ''
        else:
            current_nums += char

        # count up to "5", then start anew
        i += 1
        if i == 6 and last_group:
            nums.append(current_nums)
            remaining_body = body[index+1:]
            break
        elif i == 6:
            i = 1  # reset for next group of five

    binary_representation = ''.join(nums)
    decimal_num = int(binary_representation, 2)
    print(f"Packet represents a literal value, encodes the decimal number {decimal_num}.")
    return remaining_body, decimal_num
