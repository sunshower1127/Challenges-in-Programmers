"""

예상 대진표

토너먼트에서 a번째 참가자와 b번째 참가자는 몇번째 라운드에서 만나는가

tip : 라운드가 진행될 때마다 참가자 번호는 절반으로 줄어든다.
        시간복잡도가 낮으므로 시뮬레이션을 돌리자.
tip2 : math.ceil은 (n + 1) // 2로 대체할 수 있다.
tip3 : math.floor은 n // 2로 대체할 수 있다.
"""


def solution(n, a, b):
    cnt = 0
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        cnt += 1
    return cnt
