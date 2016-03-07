"""
http://adventofcode.com/day/3
"""
from collections import Counter


def get_data():
    with open('data/task03.txt') as f:
        data = f.read()

    return data


def move_santa(cur_pos, ch):
    if ch == '>':
        return (cur_pos[0] + 1, cur_pos[1])
    elif ch == '<':
        return (cur_pos[0] - 1, cur_pos[1])
    elif ch == '^':
        return (cur_pos[0], cur_pos[1] + 1)
    elif ch == 'v':
        return (cur_pos[0], cur_pos[1] - 1)
    else:
        raise ValueError()


def santa_procedure(moves):
    current_position = (0, 0)
    counter = Counter()
    counter[current_position] += 1

    for ch in moves:
        current_position = move_santa(current_position, ch)
        counter[current_position] += 1

    attended_houses = set(counter.keys())

    return attended_houses


def solve():
    data = get_data()

    santa_moves = [ch for idx, ch in enumerate(data) if idx % 2 == 0]
    robosanta_moves = [ch for idx, ch in enumerate(data) if idx % 2 == 1]

    total_houses = (
        santa_procedure(santa_moves) | santa_procedure(robosanta_moves))

    print('Houses attended:', len(total_houses))


if __name__ == '__main__':
    solve()
