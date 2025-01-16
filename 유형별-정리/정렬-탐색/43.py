"""

더 맵게

가장 안매운 음식 두개를 섞어서 더 매운 음식으로 만들고
이과정을 반복해서 모든 음식의 스코빌 지수가 K 이상이 되는 최소 횟수

섞은 음식의 스코빌 지수 =
    가장 맵지 않은 음식의 스코빌 지수 +
    (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

길이는 10^6

계속해서 최솟값을 뽑아내야함 -> 최소힙

tip : heapq의 default는 최소힙이다.

"""

from heapq import heapify, heappop, heappush


def solution(scoville, K):
    Cnt = 0
    heapify(scoville)

    def f(x, y):
        return x + y * 2

    while True:
        First = heappop(scoville)

        if First >= K:
            return Cnt

        if not scoville:
            return -1

        Second = heappop(scoville)
        heappush(scoville, f(First, Second))
        Cnt += 1
