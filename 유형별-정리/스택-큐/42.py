"""주식가격

가격이 떨어지지않은 기간은 몇초인지?

    -   -
  -   -
-
4 3 1 1 0
이렇게 되어있으면 4 3 1 1 0

투포인터긴 한데 원래는
10^5임. 길이가
그래서 투포인터가 아니라
메모라이제이션을 해야한다 이거죠

나보다 가격이 높은애가 히스토리에 있다?
컷이죠.
원래 이게 힙 써도 되는데
스택 써도 된다.
"""

from collections import namedtuple


def solution(prices):
    N = len(prices)
    history = []
    HistoryItem = namedtuple("HistoryItem", "i price")
    result = [0] * N

    for i, price in enumerate(prices):
        while history and history[-1].price > price:
            h = history.pop()
            result[h.i] = i - h.i

        history.append(HistoryItem(i, price))

    for h in history:
        result[h.i] = N - h.i - 1

    return result
