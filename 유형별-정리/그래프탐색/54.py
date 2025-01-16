"""
재귀. dfs

재귀 dfs 동의합니다.
0하고 1 개수를 잘 리턴해야겠네

2차원 배열안에 모든 수가 1 혹은 0 인... -> 그냥 for문 써

굳 오늘은 여기까지 풂.
"""


def solution(arr):
    cnt0 = cnt1 = 0
    N = len(arr)

    def dfs(y, x, n):
        nonlocal cnt0, cnt1

        def arr_is_all(v):
            for ny in range(y, y + n):
                for nx in range(x, x + n):
                    if arr[ny][nx] != v:
                        return False
            return True

        if arr_is_all(0):
            cnt0 += 1
            return

        if arr_is_all(1):
            cnt1 += 1
            return

        n //= 2
        dfs(y, x, n)
        dfs(y + n, x, n)
        dfs(y, x + n, n)
        dfs(y + n, x + n, n)

    dfs(0, 0, N)

    return [cnt0, cnt1]
