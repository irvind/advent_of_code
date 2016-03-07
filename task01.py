"""
http://adventofcode.com/day/1
"""


def get_data():
    with open('data/task01.txt') as f:
        data = f.read()

    return data


def solve():
    data = get_data()

    level = 0
    first_basement_enter = None
    for idx, ch in enumerate(data):
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1

        if level == -1 and first_basement_enter is None:
            first_basement_enter = idx + 1

    print('Final level:', level)
    print('First basement enter index:', first_basement_enter)


if __name__ == '__main__':
    solve()
