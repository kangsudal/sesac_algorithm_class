import sys

sys.setrecursionlimit(10 ** 9)


def find(depth):
    if depth == 10000:
        print("찾았다!")
        return

    print(f'내려가는 중.. 위치는 {depth}')

    find(depth + 1)

    print(f'올라오는 중.. 위치는 {depth}')


find(0)