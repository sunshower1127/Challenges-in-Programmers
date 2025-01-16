"""거리두기 확인하기

P사이에 거리를 보고, 이제 길찾기죠 제가 봤을때
그냥 P를 탐색하면 될거 같은데
너무 쉽긴한데 일단 풀어볼게요


"""


def 거리두기(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P" and search(place, y, x):
                return 0
    return 1


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def search(place, y, x):
    for dir in dirs:
        ny, nx = y + dir[0], x + dir[1]
        if not (0 <= ny < 5 and 0 <= nx < 5) or place[ny][nx] == "X":
            continue
        if place[ny][nx] == "P":
            return True

        for dir in dirs:
            nny, nnx = ny + dir[0], nx + dir[1]
            if (
                (nny, nnx) == (y, x)
                or not (0 <= nny < 5 and 0 <= nnx < 5)
                or place[nny][nnx] == "X"
            ):
                continue
            if place[nny][nnx] == "P":
                return True

    return False


def solution(places):
    return [거리두기(place) for place in places]
