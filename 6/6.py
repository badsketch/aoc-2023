from functools import reduce
from typing import List
from collections import namedtuple


Race = namedtuple("Race", ["time", "distance"])

def construct_races() -> List[Race]:
    with open("6_input.txt") as f:
        for line in f:
            if line.startswith("Time"):
                times = line.split(":")[1].strip().split()
                times = [int(time) for time in times]
            if line.startswith("Distance"):
                distances = line.split(":")[1].strip().split()
                distances = [int(distance) for distance in distances]

        races: List[Race] = []
        for i in range(len(times)):
            races.append(Race(times[i], distances[i]))
    return races


def calc_margin_of_error(races: List[Race]) -> int:
    errors = []
    for race in races:
        possible_wins = 0
        for milli in range(race.time + 1):
            if milli * (race.time - milli) > race.distance:
                possible_wins += 1
        errors.append(possible_wins)
    return reduce(lambda x, y: x * y, errors)


def part1() -> int:
    races = construct_races()            
    return calc_margin_of_error(races)


if __name__ == "__main__":
    print(part1())