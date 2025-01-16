"""가장 큰 정사각형 찾기

1000 * 1000 이네요 근데 하나하나 봐도 되지않나요 이러면

근데 이제 하나하나 탐색하면 시간 초과일듯 아닌가

메모라이제이션을 쓸 수 있을거 같긴한데

-> dp 접근

0 1 1 1
1 1 2 2
1 2 2 3
0 0 1 0

그냥 외워서 하는게 나을듯 dp는 발상이 바로 떠올리기 힘들다

"""


def solution(board):
    H = len(board)
    W = len(board[0])

    dp = [[0] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            dp[y][x] = board[y][x]

    max_v = 0

    for y in range(H):
        for x in range(W):
            if board[y][x] == 1:
                max_v = 1
                break

    for y in range(1, H):
        for x in range(1, W):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1

                max_v = max(max_v, dp[y][x])

    return max_v**2
