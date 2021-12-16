from parse_num_package import parse_num_package
from map_hex_to_bin import map_hex_to_bin



def decode_package(binary: str) -> (str, int):
    global version_numbers

    version = int(binary[:3], 2)
    version_numbers += version
    type_id = int(binary[3:6], 2)
    body = binary[6:]
    print("________________")
    print("Package version", version)
    print("Package type_id", type_id)

    if type_id == 4:
        return parse_num_package(body)
    else:
        print("Package represents an operator.")
        if body[0] == '0':  # checking length type id
            total_length_in_bits = int(body[1:16], 2)
            body = body[16:]
            body_subpackages = body[:total_length_in_bits]
            body = body[total_length_in_bits:]  # cut remaining body.
            print(f"Operator package of type '0'. Total length of subpackages is {total_length_in_bits}.")
            decimal_nums = []
            while len(body_subpackages) > 0:
                body_subpackages, decimal_num = decode_package(body_subpackages)
                decimal_nums.append(decimal_num)  # What to do with them?
        elif body[0] == '1':  # checking length type id
            number_of_subpackages = int(body[1:12], 2)
            print(f"Operator package of type '1'. Total number of subpackages is {number_of_subpackages}.")
            body = body[12:]
            decimal_nums = []
            for _ in range(number_of_subpackages):
                body, decimal_num = decode_package(body)
                decimal_nums.append(decimal_num)

    return body, 0  # placeholder number for part 1


with open("data.txt") as f:
    hex_string = f.readlines()[0].strip()

binary_string = ''.join([map_hex_to_bin[letter] for letter in hex_string])

version_numbers = 0
_, _ = decode_package(binary_string)
print(f"The sum of version numbers is {version_numbers}.")
