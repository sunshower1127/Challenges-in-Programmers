"""다음 큰 숫자

자기 보다 큰 수 중 2진수로 변환했을 때 1의 갯수가 같은 수 중 가장 작은 수 하나 구하기.
input : 78 -> 1001110 -> 4개
output : 83 -> 1010011 -> 4개

너무 쉬워서 패스
"""


def solution(n):
    i = n + 1
    CntN = bin(n).count("1")

    while True:
        if bin(i).count("1") == CntN:
            return i

        i += 1
