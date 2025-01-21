"""knapsack
      0  1  2  3  4  5  6  7
      0  0  0  0  0  0  0  0
6 13                   13 13
4 8
3 6
5 12

"""

N, K = map(int, input().split(" "))

items = [tuple(map(int, input().split(" "))) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    item_weight, item_value = items[y - 1]
    for x in range(1, K + 1):
        dp[y][x] = max(
            dp[y][x - 1],
            dp[y - 1][x],
            (dp[y - 1][x - item_weight] + item_value) if x - item_weight >= 0 else 0,
        )

print(dp[N][K])
