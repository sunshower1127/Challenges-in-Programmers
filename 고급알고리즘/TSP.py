import sys

input = sys.stdin.readline
INF = float("inf")


def tsp(current, visited, dp, dist):
    # 모든 도시를 방문한 경우
    if visited == (1 << n) - 1:
        return dist[current][0] if dist[current][0] > 0 else INF

    # 이미 계산된 경우
    if dp[current][visited] != -1:
        return dp[current][visited]

    dp[current][visited] = INF
    # 방문하지 않은 도시들을 방문
    for next in range(n):
        if visited & (1 << next) == 0 and dist[current][next] > 0:
            dp[current][visited] = min(
                dp[current][visited],
                tsp(next, visited | (1 << next), dp, dist) + dist[current][next],
            )

    return dp[current][visited]


# 입력
n = int(input())  # 도시의 수
dist = [list(map(int, input().split())) for _ in range(n)]  # 거리 행렬

# DP 테이블 초기화
dp = [[-1] * (1 << n) for _ in range(n)]

# 0번 도시에서 시작
answer = tsp(0, 1, dp, dist)
print(answer)
