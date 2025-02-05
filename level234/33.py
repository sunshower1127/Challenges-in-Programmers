"""포도주 시식

연속 3잔 맛보기 불가.

2잔까진 가능하다이거죠

6 10 13 9 8 1

6 10 9 8 -> 33

ooo가 안됨.

이전이 oo면 무조건 x임.

이게 만약 막잔은 무조건 마셔야한다는 조건이 붙어야하냐 이거죠

붙는게 맞긴함 근데 일단
?oo|x
?ox|o
?xo|o

근데 붙이면 굉장히 복잡해지네요 이게
붙이면 그 전에꺼가 과연 2잔째인지 체크하는 부분이 필요해짐.

간단하게 표를 만들어보죠

   6  10  13  9  8  1
0  0   6  16
1  6  10  19
2  -  16  23

dp[n][0] = max(dp[n-1])
dp[n][1] = dp[n-1][0] + current
dp[n][2] = dp[n-1][1] + current

이걸근데 압축 시킬 수 있죠 공간복잡도를

dp[n][0] = max(dp[n-1])
dp[n][1] = max(dp[n-2]) + current
dp[n][2] = max(dp[n-3]) + before + current

다 max기 때문에 하나로 압축이 가능하다 이거임

dp[n] = max(
    dp[n-1],
    dp[n-2] + drink[n],
    dp[n-3] + drink[n-1], drink[n]
)

즉,
마지막 값을 포함시키지 않는 dp는
값에 o, x가 아니라 ?가 붙음.

  ?|x
 ?x|o
?xo|o

만약 마지막을 무조건 포함시킨다면 내가 한것처럼 2차원 배열로 만드는게 맞고,
포함 안시킨다고 하면 위에 처럼 만들면 됨

"""

N = int(input())

drinks = [int(input()) for _ in range(N)]

dp: list[list[float]] = [[0] * 3 for _ in range(N + 1)]
dp[0][1] = dp[0][2] = -float("inf")

for n, drink in enumerate(drinks, start=1):
    dp[n][0] = max(dp[n - 1])
    dp[n][1] = dp[n - 1][0] + drink
    dp[n][2] = dp[n - 1][1] + drink

dp[0][0] = max(dp[-1])
result = max(dp[n][0] for n in range(N + 1))

print(result)
