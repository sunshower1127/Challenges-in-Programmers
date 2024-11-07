"""디펜스 게임

패스를 써서 최대 얼마나 버틸 수 있는가?

경우의수 인데
방향성을 가지고 있어서 dp인줄 알았는데
그냥 다 더하고 큰거 몇개 빼는거였음.

이게 if 설계할때 복잡해지면 한 번 정리해보는 시간 갖는게 좋을거같은데
그냥 텍스트로 정리해볼까


7-4 = 3
3-2 = 1
1-4 = -3 이니깐? 3, 1, 4 중에서 이제 4패스.

만약 k가 없으면? -> 끝남

그니깐 이게 -가 되버리면?
k 하나를 소모해서 제일 큰거 하나를 더하는거죠
그래도 안돼? 그러면 오버.
아니면 k가 없어? 그러면 오버.


"""

from heapq import heappop, heappush


def solution(n, k, enemies):
    max_heap = []

    for round, enemy in enumerate(enemies, 1):
        heappush(max_heap, -enemy)
        n -= enemy

        if n < 0:
            if k == 0:
                return round - 1

            k -= 1
            n += -heappop(max_heap)

            if n < 0:
                return round - 1

    return round
