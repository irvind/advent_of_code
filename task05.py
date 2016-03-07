"""
http://adventofcode.com/day/5
"""
import re
import pdb


def get_data():
    with open('data/task05.txt') as f:
        data = f.read()

    return data.strip()


def is_nice(string):
    bad_strs = ('ab', 'cd', 'pq', 'xy')
    for b in bad_strs:
        if b in string:
            return False

    vowel_count = len(re.findall(r'[aeiou]', string))
    if vowel_count < 3:
        return False

    found = False
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            found = True

    if not found:
        return False

    return True


def all_indices(li, v):
    r = []

    ind = -1
    while True:
        try:
            ind = li.index(v, ind + 1, len(li))
            r.append(ind)
        except ValueError:
            break

    return r


def is_super_nice(string):
    pairs = [string[i:i+2] for i in range(len(string) - 1)]

    found = False
    for pair in pairs:
        indices = all_indices(pairs, pair)

        for ind in indices:
            if any(abs(i - ind) > 1 for i in indices):
                found = True
                break

        if found:
            break

    if not found:
        return False

    found = False
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            found = True
            break

    if not found:
        return False

    return True


def solve(nice_func):
    c = 0
    data = get_data()
    for line in data.split('\n'):
        if nice_func(line):
            c += 1

    print('Nice strings:', c)


if __name__ == '__main__':
    solve(is_nice)
    # pdb.set_trace()
    solve(is_super_nice)
