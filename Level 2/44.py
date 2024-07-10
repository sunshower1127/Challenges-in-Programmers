"""

방문 길이

xy -5~5의 맵이 있고
UDLR로 이동함.
맵을 넘어서 이동하는건 무시되고,
이동한 길이를 구하는데, 이미 가본 길은 무시함.

이미 가본 길 체크 -> set이 바람직하겠죠.

set에 넣을 수 있는 객체는 한정되어 있음
조건 1. 변경 불가 -> 이건 그냥 내부적으로 구현
조건 2. hash값 생성 기능 -> __hash__ 메서드 구현여부

tuple, namedtuple가 거의 유일하게 set에 넣을 수 있는 컨테이너임.
list하고 dict는 변경 가능 하기 때문에 못 넣음.

아래 코드도 좀 더 복잡했으면 tuple대신 namedtuple을 사용했을듯.
"""


def solution(dirs):
    y, x = 0, 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    DirToIdx = "RULD"
    Paths = set()
    for Dir in dirs:
        i = DirToIdx.find(Dir)
        ny = y + dy[i]
        nx = x + dx[i]

        if not (-5 <= ny <= 5 and -5 <= nx <= 5):
            continue

        Paths.add(((y, x), (ny, nx)))
        Paths.add(((ny, nx), (y, x)))

        y, x = ny, nx

    return len(Paths) // 2
