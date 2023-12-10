from typing import Tuple
from functools import cmp_to_key
from collections import Counter


def camel_card_comp(line1: Tuple[str, int], line2: Tuple[str, int]) -> int:
    # check type first
    hand1 = line1[0]
    hand2 = line2[0]
    c1 = Counter(hand1) 
    c2 = Counter(hand2)
    if max(c1.values()) < max(c2.values()):
        return -1
    elif max(c1.values()) > max(c2.values()):
        return 1

    ## 3 same card case (full house vs non pair)
    if max(c1.values()) == 3:
        if min(c1.values()) < min(c2.values()):
            return -1
        elif min(c1.values()) > min(c2.values()):
            return 1
        
    ## pair case (two pairs vs 1 pair)
    if max(c1.values()) == 2:
        c1_vals = sorted(c1.values())
        c2_vals = sorted(c2.values())
        if c1_vals[-2] < c2_vals[-2]:
            return -1
        elif c1_vals[-2] > c2_vals[-2]:
            return 1

    # check individual ranks starting from first
    card_ranks = {
        "2": 1,
        "3": 2,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "T": 11,
        "J": 12,
        "Q": 13,
        "K": 14,
        "A": 15
    }

    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        if card_ranks[card1] < card_ranks[card2]:
            return -1
        elif card_ranks[card1] > card_ranks[card2]:
            return 1
    return 0


def camel_card_joker_comp(line1: Tuple[str, int], line2: Tuple[str, int]) -> int:
    # check type first
    hand1 = line1[0]
    hand2 = line2[0]
    
    # special case since there's no max value to add the count to
    if hand1 == "JJJJJ":
        hand1 = "ZZZZZ"
    if hand2 == "JJJJJ":
        hand2 = "ZZZZZ"

    c1 = Counter(hand1) 
    c2 = Counter(hand2)

    c1_j = c1.get("J", 0)
    c2_j = c2.get("J", 0)
    c1.pop("J", None)
    c2.pop("J", None)

    c1_max_key = max(c1, key=c1.get)
    c2_max_key = max(c2, key=c2.get)
    c1[c1_max_key] += c1_j
    c2[c2_max_key] += c2_j

    if max(c1.values()) < max(c2.values()):
        return -1
    elif max(c1.values()) > max(c2.values()):
        return 1

    ## 3 same card case (full house vs non pair)
    if max(c1.values()) == 3:
        if min(c1.values()) < min(c2.values()):
            return -1
        elif min(c1.values()) > min(c2.values()):
            return 1
        
    ## pair case (two pairs vs 1 pair)
    if max(c1.values()) == 2:
        c1_vals = sorted(c1.values())
        c2_vals = sorted(c2.values())
        if c1_vals[-2] < c2_vals[-2]:
            return -1
        elif c1_vals[-2] > c2_vals[-2]:
            return 1

    # check individual ranks starting from first
    card_ranks = {
        "Z": -1,
        "J": 0,
        "2": 1,
        "3": 2,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "T": 11,
        "Q": 13,
        "K": 14,
        "A": 15
    }

    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        if card_ranks[card1] < card_ranks[card2]:
            return -1
        elif card_ranks[card1] > card_ranks[card2]:
            return 1
    return 0


def part1() -> int:
    winnings = 0
    cards: Tuple[str, int]  = []
    with open("7_input.txt") as f:
        for line in f.read().splitlines():
            hand, bid = line.split()
            cards.append((hand, int(bid)))
    cards.sort(key=cmp_to_key(camel_card_comp))
    for rank, (_, bid) in enumerate(cards):
        winnings += (rank + 1) * bid
    return winnings


def part2() -> int:
    winnings = 0
    cards: Tuple[str, int]  = []
    with open("7_input.txt") as f:
        for line in f.read().splitlines():
            hand, bid = line.split()
            cards.append((hand, int(bid)))
    cards.sort(key=cmp_to_key(camel_card_joker_comp))
    for rank, (_, bid) in enumerate(cards):
        winnings += (rank + 1) * bid
    return winnings


if __name__ == "__main__":
    print(part1())
    print(part2())
