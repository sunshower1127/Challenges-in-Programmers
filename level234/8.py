"""숫자 게임

정렬은 맞았음.

근데 둘다 정렬한 상태니깐 그냥 이렇게 옆으로 들어서 맞추기만 하면 된다.

A 7 5 3 1
B 8 6 2 2

옆으로 맞출때 찢어져도 된다.

어렵네요 ㄹㅇ

Tip: Error가 어디서 나는지 모르겠으면 try except로 묶고 print(locals())하면 에러 당시의 컨텍스트를 볼 수 있음.
"""


def solution(A, B):
    N = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt = 0

    a = b = 0
    while a < N:
        if A[a] < B[b]:
            a += 1
            b += 1
        else:
            a += 1
            cnt += 1

    return N - cnt
