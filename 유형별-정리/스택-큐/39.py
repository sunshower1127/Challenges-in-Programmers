"""뒤에 있는 큰 수 찾기

자신보다 뒤에 있는 숫자중에서 나보다 크면서 가장 가까이 있는 수.

그러면 탐색이 이뤄줘야하는데?
문제는 10^6이면 내림차순으로 숫자들이 있다고 할때 어우...
시간 초과임.

투포인터의 최적화는? 스택이나 큐다.

2 3 3 5
인덱스도 같이 넣어야겠는데
[3, 3]

스택이 아니라 heap으로 하면

핵심은 원래는 heap으로 해야 맞는데
어차피 ^ 로 메모리에 값이 안쌓인다는거임. 맞죠.
그래서 stack으로 해도 대체가 된다.
"""

from heapq import heappop, heappush


def solution(numbers):
    result = [-1] * len(numbers)
    minheap = []
    for index, num in enumerate(numbers):
        while minheap and minheap[0][0] < num:
            v, i = heappop(minheap)
            result[i] = num

        heappush(minheap, (num, index))

    return result
