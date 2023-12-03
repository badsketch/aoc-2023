from typing import List


def is_symbol(c: str) -> bool:
    return not c.isdigit() and c != "."


def convert_input_to_2d_schematic() -> List[List[str]]:
    schematic = []
    with open("3_input.txt") as f:
        for line in f.read().splitlines():
            schematic_line = []
            for unit in line:
                schematic_line.append(unit)
            schematic.append(schematic_line)
    return schematic


def expand_number(schematic: List[List[str]], start_row: int, start_col: int) -> int:
    number = ""
    # go left
    while schematic[start_row][start_col].isdigit() and start_col >= 0:
        start_col -= 1
    # go right
    start_col += 1
    while start_col < len(schematic[start_row]) and schematic[start_row][start_col].isdigit():
        number += schematic[start_row][start_col]
        # overwrite so it doesn't get recorded when looking at a nearby symbol
        schematic[start_row][start_col] = "."
        start_col +=1
    return int(number)


DIRECTIONS = [
    (-1,  0), # up
    (-1,  1), # up/right
    ( 0,  1), # right
    ( 1,  1), # down/right
    ( 1,  0), # down
    ( 1, -1), # down/left
    ( 0, -1), # left
    (-1, -1), # up/left
]


def find_parts(schematic: List[List[str]]) -> List[int]:
    parts = []
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if is_symbol(schematic[row][col]):
                # check directions
                for rdelta, cdelta in DIRECTIONS:
                    if 0 <= row + rdelta < len(schematic) and 0 <= col + cdelta < len(schematic[row]):
                        if schematic[row + rdelta][col + cdelta].isdigit():
                            parts.append(expand_number(schematic, row + rdelta, col + cdelta))

    return parts
                            

def is_gear(c: str) -> bool:
    return c == "*"


def find_gear_ratios(schematic: List[List[str]]) -> List[int]:
    gear_ratios = []
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if is_gear(schematic[row][col]):
                # check adjacentt to two parts
                adjacent_parts = []
                for rdelta, cdelta in DIRECTIONS:
                    if 0 <= row + rdelta < len(schematic) and 0 <= col + cdelta < len(schematic[row]):
                        if schematic[row + rdelta][col + cdelta].isdigit():
                            adjacent_parts.append(expand_number(schematic, row + rdelta, col + cdelta))
                    if len(adjacent_parts) > 2:
                        break
                if len(adjacent_parts) == 2:
                    gear_ratios.append(adjacent_parts[0] * adjacent_parts[1])
    return gear_ratios


def part1():
    schematic = convert_input_to_2d_schematic()
    parts = find_parts(schematic)
    return sum(parts)


def part2():
    schematic = convert_input_to_2d_schematic()
    gear_ratios = find_gear_ratios(schematic)
    return sum(gear_ratios)


if __name__ == "__main__":
    print(part1())
    print(part2())
