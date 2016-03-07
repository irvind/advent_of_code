"""
http://adventofcode.com/day/4
"""
import hashlib


def solve(find):
    c = 1
    while True:
        s = 'ckczppom' + str(c)
        digest = hashlib.md5(s.encode('ascii')).hexdigest()

        if digest[:len(find)] == find:
            break

        c += 1

    return c


if __name__ == '__main__':
    print(solve('00000'))
    print(solve('000000'))
