from typing import List


def extrapolate(nums: List[int]) -> int:
    steps: List[List[int]] = [nums]
    # build
    # by finding difference until all are zero
    while not all_zero(steps[-1]):
        steps.append(build_diff(steps[-1]))

    # predict 
    # starting from last sequence and work back to origin
    for i in range(len(steps) - 1, 0, -1):
        prediction = steps[i][-1] + steps[i - 1][-1]
        steps[i - 1].append(prediction)
    
    return steps[0][-1]


def extrapolate_start(nums: List[int]) -> int:
    steps: List[List[int]] = [nums]
    # build
    # by finding difference until all are zero
    while not all_zero(steps[-1]):
        steps.append(build_diff(steps[-1]))

    # predict 
    # starting from last sequence and work back to origin at start
    for i in range(len(steps) - 1, 0, -1):
        prediction = steps[i - 1][0] - steps[i][0]
        steps[i - 1].insert(0, prediction)
    
    return steps[0][0]


def all_zero(nums: List[int]) -> bool:
    return all(not num for num in nums)


def build_diff(nums: List[int]) -> List[int]:
    diffs = []
    for i in range(1, len(nums)):
        diffs.append(nums[i] - nums[i - 1])
    return diffs


def part1() -> int:
    oasis_total = 0
    with open("9_input.txt") as f:
        for line in f.read().splitlines():
            nums = [int(num) for num in line.split()]
            oasis_total += extrapolate(nums)
    return oasis_total


def part2() -> int:
    oasis_prev_total = 0
    with open("9_input.txt") as f:
        for line in f.read().splitlines():
            nums = [int(num) for num in line.split()]
            oasis_prev_total += extrapolate_start(nums)
    return oasis_prev_total


if __name__ == "__main__":
    print(part1())
    print(part2())