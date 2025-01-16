"""쿼드압축 후 개수 세기

4둥분해서 확인하고 4등분해서 확인하고.... 무한반복

이게 근데 dfs라고 볼 수 있나? 그냥 분할정복 아닌가?
흠..


"""


def solution(arr):
    N = len(arr)
    stack = []
    result = [0, 0]

    stack.append(((0, 0), N))

    while stack:
        (y, x), n = stack.pop()

        target = arr[y][x]
        if all(arr[y + dy][x + dx] == target for dy in range(n) for dx in range(n)):
            result[target] += 1
            continue

        n //= 2
        stack.append(((y, x), n))
        stack.append(((y + n, x), n))
        stack.append(((y, x + n), n))
        stack.append(((y + n, x + n), n))

    return result
