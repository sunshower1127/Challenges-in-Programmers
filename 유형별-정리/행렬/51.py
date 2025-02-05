"""[1차] 프렌즈 4블록

쉽지 않았음 ㄹㅇ

2*2를 계속 터뜨려서 총 몇개 터졌나 계산하는건데

deque쓰기엔 또 탐색이 많아서 복잡했고
차라리 list로 최적화 최대한 하는게 좋아보였음.

거의 한 40분 걸림. 후...

sum에서 True는 1, False는 0으로 계산해주나봄. 체크해주고.
count보다 유용할듯 암튼 패스

아니 근데 if a == b == c == d: 이게 된다고?
a = b = c = d = 1 도 원래 안돼야하는데
파이썬에서 특별히 지원해주는 기능이라네요.
"""


def GetBomb(H, W, Mat):
    """Input : 현재 매트릭스
    Output : 터뜨려야할 좌표들이 담긴 매트릭스 -> 터뜨릴 부분은 True, 아닌 부분은 False
    """
    IsBomb = [[False] * H for _ in range(W)]

    for y in range(H - 1):
        for x in range(W - 1):
            v = (Mat[x][y], Mat[x + 1][y], Mat[x][y + 1], Mat[x + 1][y + 1])
            if v[0] and v[0] == v[1] == v[2] == v[3]:
                IsBomb[x][y] = IsBomb[x + 1][y] = IsBomb[x][y + 1] = IsBomb[x + 1][
                    y + 1
                ] = True

    return IsBomb


def GetBombCnt(Mat):
    return sum(sum(Col) for Col in Mat)


def solution(H, W, Board):
    Board = list(zip(*reversed(Board)))
    Cnt = 0

    while True:
        BombMat = GetBomb(H, W, Board)
        BombCnt = GetBombCnt(BombMat)
        if BombCnt == 0:
            break

        Cnt += BombCnt

        for x in range(W):
            NewCol = []
            for y in range(H):
                if not BombMat[x][y]:
                    NewCol.append(Board[x][y])
            NewCol += [""] * (H - len(NewCol))
            Board[x] = NewCol

    return Cnt
