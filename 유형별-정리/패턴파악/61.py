"""

마법의 엘리베이터

0층부터 (-층은 없음)
10^8층
에서 0층으로 가려면 최소 몇번?

근데 자릿수라서 그냥 그리디 하면 될듯

25라고 할때, 20 + 5기도 하지만, 30 - 5기도 하죠
즉 앞에 자리가

16이면 -> 10 + 6 or 20 - 4

6부터 9까진 특수하게 계산하는게 맞는듯

5일때 그냥 넘기는게 아니라,
앞에 1을 추가하는게 이득일지, 아닐지를 판단...

tip: 몇몇 케이스를 제외하고 풀리는 경우 -> 특수한 경우를 파고들자. -> 여 문제는 5에 대한 계산이 중요했음.
    이해가 안돼도 그냥 케이스를 막 나눠보면 풀릴 수도 있음.

"""


def solution(storey):
    storey = list(map(int, reversed(str(storey))))
    storey.append(0)

    for i in range(len(storey) - 1):
        if storey[i] == 5:
            if storey[i + 1] >= 5:
                storey[i + 1] += 1
        elif storey[i] > 5:
            storey[i] = 10 - storey[i]
            storey[i + 1] += 1

    return sum(storey)


def solution_by_ai(storey):
    storey = list(map(int, reversed(str(storey))))
    storey.append(0)
    moves = 0

    for i in range(len(storey) - 1):
        if storey[i] > 5 or (storey[i] == 5 and storey[i + 1] >= 5):
            moves += 10 - storey[i]
            storey[i + 1] += 1
        else:
            moves += storey[i]

    return moves
