"""

숫자 변환하기

x->y로 변환
1. x + n
2. 2x
3. 3x

최소 연산 횟수는?

덧셈 곱셈의 우선순위가 존재하지 않음 -> 그리디 아님
dp가 맞지 않나 bfs보다는?

흠. dp하고 탐색하고 결국 본질은 같다 이건가


"""


def solution(x, y, n):
    MAX = 10**6
    Dp = [MAX] * (y + 1)
    Dp[x] = 0
    for i in range(x + 1, y + 1):
        Dp[i] = (
            min(
                Dp[i - n] if i - n >= 0 else MAX,
                Dp[i // 2] if i % 2 == 0 else MAX,
                Dp[i // 3] if i % 3 == 0 else MAX,
            )
            + 1
        )

    return Dp[y] if Dp[y] < MAX else -1
