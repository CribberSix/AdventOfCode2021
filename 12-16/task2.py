from parse_num_package import parse_num_package
from map_hex_to_bin import map_hex_to_bin


def decode_package(binary: str) -> (str, int):
    version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)
    body = binary[6:]
    print("________________")
    print("Package version", version)
    print("Package type_id", type_id)

    if type_id == 4:  # Package representing a single decimal number
        return parse_num_package(body)

    else:
        decimal_nums = []
        if body[0] == '0':  # checking length type id
            total_length_in_bits = int(body[1:16], 2)
            body = body[16:]
            body_subpackages = body[:total_length_in_bits]
            body = body[total_length_in_bits:]  # cut remaining body.
            print(f"Operator package of type '0'. Total length of subpackages is {total_length_in_bits}.")
            while len(body_subpackages) > 0:
                body_subpackages, decimal_num = decode_package(body_subpackages)
                decimal_nums.append(decimal_num)  # What to do with them?
        elif body[0] == '1':  # checking length type id
            number_of_subpackages = int(body[1:12], 2)
            print(f"Operator package of type '1'. Total number of subpackages is {number_of_subpackages}.")
            body = body[12:]
            for _ in range(number_of_subpackages):
                body, decimal_num = decode_package(body)
                decimal_nums.append(decimal_num)

        print(f">>>> Numbers contained: {decimal_nums}")
        print(">>>> Parsing the operator type. ")
        if type_id == 0:
            result = sum(decimal_nums)
            print(f">>>> Operator Type: sum. Result: {result}")
        elif type_id == 1:
            result = 1
            for num in decimal_nums:
                result = result * num
            print(f">>>> Operator Type: product. Result: {result}")
        elif type_id == 2:
            result = min(decimal_nums)
            print(f">>>> Operator Type: minimum. Result: {result}")
        elif type_id == 3:
            result = max(decimal_nums)
            print(f">>>> Operator Type: maximum. Result: {result}")
        elif type_id == 5:
            result = 1 if decimal_nums[0] > decimal_nums[1] else 0
            print(f">>>> Operator Type: greater_than. Result: {result}")
        elif type_id == 6:
            result = 1 if decimal_nums[0] < decimal_nums[1] else 0
            print(f">>>> Operator Type: less_than. Result: {result}")
        elif type_id == 7:
            result = 1 if decimal_nums[0] == decimal_nums[1] else 0
            print(f">>>> Operator Type: equal_to. Result: {result}")

    # return the remaining body and the result of the operator.
    return body, result


with open("data.txt") as f:
    hex_string = f.readlines()[0].strip()

binary_string = ''.join([map_hex_to_bin[letter] for letter in hex_string])

_, result = decode_package(binary_string)
print(f"\n\nThe final resulting number is '{result}'.")
