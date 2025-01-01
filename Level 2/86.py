"""후보키

후보키 구하는게 나올줄은 몰랐는데

일단 유일성을 띄는 집합중에서 최소를 구해야함.
어.. 후보는 이제 2^20 -> 10^8 이라서 브루트도 될것...같...지 않긴해요 굳이

개수를 1개부터 시작한다?
OOXX
2개
3개
4개

여기서 잘 가지만 쳐 나가면 되지 뭐

tip : 이렇게 combination이 1부터 n까지 다 계산하는 경우는 2^n이니깐 비트 마스킹을 쓰면 편해진다.
"""

from itertools import combinations


def isunique(tuples):
    return len(tuples) == len(set(tuples))


def is_sub(comb, cand):  # (0, 1) (0)
    return len(comb) - len(cand) == len(set(comb) - set(cand))


def is_ok(candidates, comb):
    for cand in candidates:
        if is_sub(comb, cand):
            return False
    return True


def solution(relation):
    rows_n = len(relation)  # 6
    cols_n = len(relation[0])  # 4
    candidates = []
    for i in range(1, cols_n + 1):  # 1 ~ 4 -> 1
        combs = combinations(
            list(range(cols_n)), i
        )  # [0, 1, 2, 3] 에서 1개 -> [(0), (1), (2), (3)]
        for comb in combs:  # (0)
            if not is_ok(candidates, comb):
                continue  # 굳
            tr = list(zip(*relation))  # 세로로
            trr = list(zip(*[tr[j] for j in comb]))

            if isunique(list(trr)):
                candidates.append(comb)

    return len(candidates)
