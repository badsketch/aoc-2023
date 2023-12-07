from functools import reduce
from typing import List
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor


Race = namedtuple("Race", ["time", "distance"])

def construct_races() -> List[Race]:
    with open("6_input2.txt") as f:
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


def calc_total_wins(race: Race) -> int:
    wins = 0
    futures = []
    with ThreadPoolExecutor() as ex:
        BATCH_SIZE = 1000000
        for i in range(0, race.time + 1, BATCH_SIZE):
            futures.append(ex.submit(calc_win, i + 1, min(race.time, i + BATCH_SIZE), race.time, race.distance))
    
    for future in futures:
        wins += future.result()
    return wins


def calc_win(start: int, end: int, time: int, dist: int) -> int:
    wins = 0
    for milli in range(start, end + 1):
        if milli * (time - milli) > dist:
            wins += 1
    return wins


def part1() -> int:
    races = construct_races()            
    return calc_margin_of_error(races)


def part2() -> int:
    race = construct_races()[0]
    return calc_total_wins(race)


if __name__ == "__main__":
    # print(part1())
    print(part2())