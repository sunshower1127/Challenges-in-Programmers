"""혼자 놀기의 달인

숫자를 섞고(1~n)
index를 1부터 붙임.

그중에 아무거나 하나 까서 안에 있는 숫자가 이제 인덱스가 되서
계속 돌다가 사이클이 생기는 순간 1번 종료 -> 연 상자수 체크
또 하나 까서 멈출때까지 -> 연 상자수 체크
두 상자수를 곱하면 끝.

이걸 최고 점수를 구해야함.

두개의 랜덤을 클릭해야한다는 건데

100 * 100 * 100 이니깐 그냥 브루트 씁시다.

이게 그냥 화살표 덩어리들이네 무조건

사이클 덩어리들임

근데 최적화 일단 미루고
이게 2가지 선택을 할 수 ㅇㅆ음.
그래프 2개를 각각 선택할 것이냐
아니면 그래프 1개를 반을 쪼개서 사용할 것이냐

tip: 꼭 문제에서 첫번째 상자 이러면서 index + 1 로 계산해야하는것들 있는데 헷갈리지말게 그냥 다 1씩 뺴고 시작해도 됨.
"""


def solution(cards):
    visited = set()
    lengths = []
    i = 0
    l = 0
    while True:
        if i + 1 in visited:
            lengths.append(l)
            l = 0
            remaining = set(cards) - visited
            if not remaining:
                break
            i = next(iter(remaining)) - 1
            continue

        visited.add(i + 1)
        l += 1
        i = cards[i] - 1

    if len(lengths) == 1:
        return 0

    lengths.sort(reverse=True)
    return lengths[0] * lengths[1]
