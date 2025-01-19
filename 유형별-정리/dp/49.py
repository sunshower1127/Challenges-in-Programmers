"""숫자 변환하기

x->y

x + n
x * 2
x * 3

최소 연산 횟수요?

dp네
왜냐면 방향성이 증가하는 쪽으로만 있으니깐 ㅇㅇ

1
2
3
4
5


"""


def solution(x, y, n):
    dp = [float("inf")] * (y + 1)
    dp[x] = 0

    for i in range(x + 1, y + 1):
        dp[i] = (
            min(
                dp[i - n] if i - n >= 0 else float("inf"),
                dp[i // 2] if i % 2 == 0 else float("inf"),
                dp[i // 3] if i % 3 == 0 else float("inf"),
            )
            + 1
        )

    return dp[y] if dp[y] != float("inf") else -1
