"""

카펫

칸이 n * m 개 있음
바깥 테두리칸은 갈색, 안쪽은 전부 노란색.

갈색 칸수랑 노란칸수가 주어졌을때 [n, m] 리턴

"""


def solution(brown, yellow):
    C1 = brown // 2 + 2
    C2 = brown + yellow
    for Height in range(3, int(C2**0.5) + 1):
        Weight = C1 - Height
        if Weight * Height == C2:
            return [Weight, Height]
