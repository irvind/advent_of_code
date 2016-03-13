import re
import pdb


def get_data():
    with open('data/task06.txt') as f:
        data = f.read()

    return data.strip()


def perform_action(field, action, rect):
    for i in range(rect[0][0], rect[1][0] + 1):
        for j in range(rect[0][1], rect[1][1] + 1):
            if action == 'turn on' and field[i][j] % 2 == 0:
                field[i][j] += 1
            elif action == 'turn off' and field[i][j] % 2 == 1:
                field[i][j] += 1
            elif action == 'toggle':
                field[i][j] += 1


def solve():
    field = [
        [0 for i in range(1000)]
        for i in range(1000)
    ]

    data = get_data()
    for line in data.split('\n'):
        line_regex = r'([^\d+]+)(\d+),(\d+) through (\d+),(\d+)'
        action, x, y, a, b = re.search(line_regex, line).groups()
        action = action.strip()

        perform_action(
            field,
            action,
            ((int(x), int(y)), (int(a), int(b)))
        )

    c = 0
    for i in range(1000):
        for j in range(1000):
            if field[i][j] % 2 == 1:
                c += 1

    print('Lights count:', c)


if __name__ == '__main__':
    solve()
