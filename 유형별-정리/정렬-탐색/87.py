"""퍼즐 게임 챌린지

n개의 퍼즐

왓 숙련도의 최솟값?

근데 어.. 패턴을 파악해봐야겠죠

숙련도가 1이면

1-1 * (2+0) + 2
5-1 * (4+2) + 4
3-1 * (7+4) + 7

max(0, level - diffs[n]) * sum(times[n] + times[n-1]) + times[n]
이건데?
10^16 ->
2^40이면 40번이면 된다 이거죠

어 일단 반씩 나눠가면서 탐색하는게 제일 가능성 있긴함.


숙련도가 2면
2-1 *

limit이 너무 커서 n도 안됨. 무조건 한번에 알아내야함.
1 2 3


3 2 1 이렇게 존재함 일단.

3을 찾아야됨

바이너리 탐색이 까다로웠는데
1. 정렬이 오름차순으로 되어있는지 내림차순으로 되어있는지 파악해야함
2. while left != right 가 아니라 left <= right로 해야함. -> left가 1이고 right가 2면 둘이 엇갈려질 수 있음.
3. 바이너리 탐색에서 찾는 값이 정확하게 존재하지 않을 수 있을때 -> min값이든 max값이든 한쪽만 +1해서 비교해줘야함
즉
바이너리 탐색 tip -> 이게 찾는 값이 없어서 근사값을 구해야할때, while left <= right 하고 mid +- 1 비교해주는게 귀찮은데
-> 그냥 근사값에 대한 아주작은 시나리오를 생각해보면 된다.

TODO: 풀어보기
"""


def solution(diffs, times, limit):
    N = len(diffs)

    def get_two(n):
        if n == 0:
            return times[0]
        return times[n - 1] + times[n]

    def get(level):
        return sum(max(0, diffs[n] - level) * get_two(n) + times[n] for n in range(N))

    left = 1
    right = 10**15
    while left <= right:
        level = (left + right) // 2
        v = get(level)
        if v == limit:
            return level
        if v < limit:
            right = level - 1
        else:
            left = level + 1

    if get(level) <= limit:
        return level
    else:
        return level + 1
