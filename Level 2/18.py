"""

연속 부분 수열 합의 개수

원형 수열이 있음. 길이가 1인 서브셋, 2인, ... N인 서브셋의 합들의 중복되지않는 개수

tip : 원형수열은 *로 늘려서 풀면 편할때가 있고, index에 /랑 %를 쓰면 편할때가 있다.
"""


def solution(elements):
    Set = set()
    N = len(elements)
    elements = elements * 2
    for Len in range(1, N + 1):
        for i in range(N):
            Set.add(sum(elements[i : i + Len]))

    return len(Set)
