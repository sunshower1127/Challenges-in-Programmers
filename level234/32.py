"""N으로 표현

N과 number가 주어짐.

number를 여러개의 N과 사칙연산으로 표현할때(floordiv)

흠...

N을 최소로 사용해야함.

괄호는 자유임. -> 사칙연산의 순서는 자유

N을 여러개 이어붙여도됨.
...

12하고 5가 있다고 봅시다.

1개
5

2개
5+5 = 10
5-5 = 0 (이건 제외)
5//5 = 1
5*5 = 25
55 = 55
4개의 경우의 수가 나오죠?
1, 10, 25, 55

3개
n+5
n-5
5-n
n//5
5//n
n*5

1 2

555

이게 만약 전에 나왔던 값이면 폐기하고, 전에 안나왔던 값이면 저장하고.

4개엔
1 3
2 2
3 1

이렇게 조합될 수 있겠죠

크기 제한은 없음

그냥 하는거죠 뭐

근데 음수는 만들어 봤자임 음수는 제외해도 될듯

"""

import operator as op
from functools import reduce


def calculate(set1, set2, target_num):
    new_set = set()

    for item1 in set1:
        for item2 in set2:
            large_one, small_one = max(item1, item2), min(item1, item2)

            cur_set = {
                large_one + small_one,
                large_one - small_one,
                large_one * small_one,
                large_one // small_one,
            }

            if target_num in cur_set:
                return cur_set

            new_set |= cur_set

    return new_set


def solution(N, target_num):
    dp = [set() for _ in range(9)]
    dp[0].add(0)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        if target_num in dp[i]:
            return i

        for left in range(1, i // 2 + 1):
            right = i - left

            new_set = calculate(dp[left], dp[right], target_num)
            if target_num in new_set:
                return i

            dp[i] |= new_set

        dp[i] -= reduce(op.ior, dp[:i])

    return -1
