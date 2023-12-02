from typing import Tuple

def get_left_digit(line: str) -> Tuple[int, int]:
    idx = 0
    while idx < len(line):
        if line[idx].isdigit():
            return int(line[idx]), idx
        idx += 1
    return -1, len(line) - 1


def get_right_digit(line: str) -> Tuple[int, int]:
    idx = len(line) - 1
    while idx >= 0:
        if line[idx].isdigit():
            return int(line[idx]), idx
        idx -= 1
    return -1, 0


def part1() -> None:
    total = 0
    with open("1_input.txt") as f:
        for line in f.read().splitlines():
            left, _ = get_left_digit(line)
            right, _ = get_right_digit(line)
            calibration_val = int(str(left) + str(right))
            total += calibration_val
    print(total)

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

def get_left_number(line: str) -> Tuple[int, int]:
    index = len(line) - 1
    number = None
    for digit in digits.keys():
        idx = line.find(digit)
        if idx >= 0 and idx < index:
            number = digits[digit]
            index = idx
    return number, index 

def get_right_number(line: str) -> Tuple[int, int]:
    index = 0
    number = None
    for digit in digits.keys():
        idx = line.rfind(digit)
        if idx >=0 and idx > index:
            number = digits[digit]
            index = idx
    return number, index

def part2() -> None:
    total = 0
    with open("1_input.txt") as f:
        for line in f.read().splitlines():
            digit_left, ldigit_idx = get_left_digit(line)
            number_left, lnumber_idx = get_left_number(line)
            if lnumber_idx < ldigit_idx:
                left = number_left
            else:
                left = digit_left

            digit_right, rdigit_idx = get_right_digit(line)
            number_right, rnumber_idx = get_right_number(line)
            if rnumber_idx > rdigit_idx:
                right = number_right
            else:
                right = digit_right
            
            calibration_val = int(str(left) + str(right))
            total += calibration_val
    print(total)
            
    

if __name__ == "__main__":
    # part1()
    part2()