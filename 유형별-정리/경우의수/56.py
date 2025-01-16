"""
모든 경우의수 나열?
길이가 최대 7
dfs로 그냥 전부 돌아보면서, 각 부분마다 체크하기.
소수판별은 그냥 9999999 -> 10^7 이니깐 nlogn에 들어감.

쉽지않았음..
중복된 애들을 dfs 돌려야해서...
익숙하지 않아서 좀 많이 비효율적인 코드가 된거 같은데
다음에 다른 사람들 풀이나 ai풀이 보면서 정리해봅시다.
22분 걸림
"""


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False

    return True


def solution(nums):
    # 17
    N = len(nums)
    # 2
    path = []  # i 담기
    prime_set = set()

    def dfs(n):
        if n != 0 and is_prime(path_num := int("".join(nums[i] for i in path))):
            prime_set.add(path_num)

        if n == N:
            return

        for i in range(N):
            if n == 0 and nums[i] == "0":
                continue
            if i not in path:
                path.append(i)
                dfs(n + 1)
                path.pop()

    dfs(0)
    return len(prime_set)


#  AI 발 코드

from itertools import permutations


def is_prime2(num):
    if num <= 1:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def solution2(nums):
    prime_set = set()
    N = len(nums)

    for length in range(1, N + 1):
        for perm in permutations(nums, length):
            num = int("".join(perm))
            if is_prime2(num):
                prime_set.add(num)

    return len(prime_set)
