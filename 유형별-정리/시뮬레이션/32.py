"""타겟 넘버

브루트 문제임 그냥 전형적인.

"""


def solution(numbers, target):
    N = len(numbers)
    cnt = 0
    for i in range(1 << N):
        is_pos = [bool(i & 1 << j) for j in range(N)]
        if sum(num if pos else -num for num, pos in zip(numbers, is_pos)) == target:
            cnt += 1

    return cnt
