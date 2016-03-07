"""
http://adventofcode.com/day/2
"""


def get_data():
    with open('data/task02.txt') as f:
        data = f.read()

    return data.strip()


def present_wrap_surface(l, w, h):
    sides = [l * w, w * h, h * l]
    summ = sum([s * 2 for s in sides])
    summ += min(sides)
    return summ


def ribbon_required(l, w, h):

    def perim(a, b):
        return a * 2 + b * 2

    perimeters = [
        perim(l, w),
        perim(w, h),
        perim(h, l),
    ]

    return l * w * h + min(perimeters)


def extract_sides(line):
    l, w, h = [int(i) for i in line.split('x')]
    return l, w, h


def solve():
    data = get_data()

    total_surface = sum([
        present_wrap_surface(*extract_sides(line))
        for line in data.split('\n')
    ])

    total_ribbon = sum([
        ribbon_required(*extract_sides(line))
        for line in data.split('\n')
    ])

    print('Wrapping paper:', total_surface)
    print('Ribbon:', total_ribbon)


if __name__ == '__main__':
    solve()
