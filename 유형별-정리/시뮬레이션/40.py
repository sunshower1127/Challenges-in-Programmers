"""방문 길이

이건 시뮬레이션이라고 보는게 맞지 않나?
중복되는거 없앤다니깐 집합이라고도 볼 수 있겠고

"""


def solution(dirs):
    path = set()
    y, x = 0, 0
    dydx = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

    for dy, dx in (dydx[dir] for dir in dirs):
        ny = y + dy
        nx = x + dx

        if not (-5 <= ny <= 5 and -5 <= nx <= 5):
            continue

        path.add(((y, x), (ny, nx)))
        path.add(((ny, nx), (y, x)))
        y, x = ny, nx

    return len(path) // 2
