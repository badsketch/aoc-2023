def part1() -> int:
    with open("4_input.txt") as f:
        total_pts = 0
        for line in f.read().splitlines():
            _, numbers_stuff = line.split(":") # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            winning_numbers_stuff, given_numbers_stuff = numbers_stuff.split("|") # 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            winning_numbers = set(winning_numbers_stuff.split()) # {41 48 83 86 17}
            given_numbers = given_numbers_stuff.split() # [83 86  6 31 17  9 48 53]
            pts_multiplier = 0
            for number in given_numbers:
                if number in winning_numbers:
                    pts_multiplier += 1
            
            if pts_multiplier:
                total_pts += 2 ** (pts_multiplier - 1)
        
        return total_pts


def part2() -> int:
    with open("4_input.txt") as f:
        cards = {}
        # first pass default all copies to 1
        for line in f.read().splitlines():
            card_stuff, numbers_stuff = line.split(":")
            card_id = int(card_stuff.split()[1])
            winning_numbers_stuff, given_numbers_stuff = numbers_stuff.split("|")
            winning_numbers = set(winning_numbers_stuff.split())
            given_numbers = given_numbers_stuff.split()

            cards[card_id] = 1

        # second pass increment based on number of copies
        f.seek(0)
        for line in f.read().splitlines():
            card_stuff, numbers_stuff = line.split(":")
            card_id = int(card_stuff.split()[1])
            winning_numbers_stuff, given_numbers_stuff = numbers_stuff.split("|")
            winning_numbers = set(winning_numbers_stuff.split())
            given_numbers = given_numbers_stuff.split()

            next_copies = 0
            for number in given_numbers:
                if number in winning_numbers:
                    next_copies += 1

            for copy in range(1, next_copies + 1):
                cards[card_id + copy] += cards[card_id]
        
    return sum(cards.values())


if __name__ == "__main__":
    print(part1())
    print(part2())