"""혼자서 하는 틱택토

OOOXOX 라거나
승리한지도 모름

암튼 이게 제대로된 틱택토인지 판단할 수 있어야함.

OOO
XX.
X..


충분히 가능하죠

O가 먼저여야하고.
흠

되게 쉬워보이는데 그냥
1. O하고 X 개수 -> cnt(O) == cnt(X) or cnt(X)+1
2. O하고 X가 동시에 정답이면 안됨

이 두개만 해볼까
3. 한쪽이 연결이 안되어 있는데 정답이 2개이상인경우


일단 9개잖아.
그럼 O는 최대 5개, X는 최대 4개 쓸 수 있음.

꽉 채웠을떄?
OOX
XOO
OXX

아직 승부가 안난경우 -> 얘가 유일한데

tip: 아 zip에서 자꾸 실수가 나오네
이게 문자열 배열을 zip(*) 하면 문자열이 나오는게 아니라 튜플이 나옴.
"""


def cnt(board, mark):
    return sum(line.count(mark) for line in board)


def has_score(board, mark):
    cnt = 0
    if any(line == mark * 3 for line in board):
        cnt += 1
    if any("".join(line) == mark * 3 for line in zip(*board)):
        cnt += 1
    if "".join((board[0][0], board[1][1], board[2][2])) == mark * 3:
        cnt += 1
    if "".join((board[0][2], board[1][1], board[2][0])) == mark * 3:
        cnt += 1
    return cnt


def solution(board):
    o_cnt = cnt(board, "O")
    x_cnt = cnt(board, "X")

    o_win = has_score(board, "O")
    x_win = has_score(board, "X")

    if not o_win and not x_win:
        if o_cnt in [x_cnt, x_cnt + 1]:
            return 1
        return 0

    if o_win and not x_win:
        if o_cnt == x_cnt + 1:
            return 1
        return 0

    if not o_win and x_win:
        if o_cnt == x_cnt:
            return 1
        return 0

    if o_win and x_win:
        return 0
