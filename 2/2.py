from collections import defaultdict


def transform_input() -> dict:
    """
    Turns:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    To:
    {
        1: {
            blue: [3, 6],
            red: [4, 1],
            green: [2, 2]
        }
    }
    """
    games = defaultdict(lambda: defaultdict(lambda: [0]))
    with open("2_input.txt") as f:
        for line in f.read().splitlines():
            [gid_stuff, all_rounds_stuff] = line.split(":")
            gid = int(gid_stuff.split(" ")[1]) # Game 1
            rounds_stuff = all_rounds_stuff.split(";")# 3 blue, 4 red; 1red, 2 green, 6 blue; 2 green
            for round in rounds_stuff: # 3 blue, 4 red
                cube_counts = round.split(",") # 3 blue
                for cube_count in cube_counts:
                    [count, color] = cube_count.strip().split(" ") # [3, blue]
                    games[gid][color].append(int(count))
    return games

            
def part1() -> None:
    games = transform_input()
    # 12 red, 13 green 14 blue
    gids = 0
    # convert to max values
    for gid, cubes in games.items():
        if max(cubes["red"]) <= 12 and max(cubes["green"]) <= 13 and max(cubes["blue"]) <= 14:
            gids += gid
    return gids


def part2() -> None:
    games = transform_input()
    powers = 0
    for cubes in games.values():
        powers += max(cubes["red"]) * max(cubes["green"]) * max(cubes["blue"])
    return powers


if __name__ == "__main__":
    # print(part1())
    print(part2())