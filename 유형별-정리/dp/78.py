"""가장 큰 정사각형 찾기

0 1 1 1
1 1 2
1
0

그거 알아? 이게 나야

dp는 방향성이다. 방향성이 여기는 오른쪽아래 즉 대각선인데
어차피 왼쪽, 왼쪽위, 위 이렇게 한칸씩만 보면 되기때문에
그냥 탐색을 x->y 순으로 하면 됨.

"""


def solution(board):
    height = len(board)
    width = len(board[0])

    dp = [row[:] for row in board]

    for y in range(1, height):
        for x in range(1, width):
            if dp[y][x] == 0:
                continue
            dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1

    return max(max(row) for row in dp) ** 2
