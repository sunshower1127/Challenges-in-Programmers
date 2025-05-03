"""숫자의 표현
1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15

3*5
5*3
7.5*2
15*1

center * 개수 = 15

역시 자연수는 소수점으로 막 계산하는것보단, 홀수 짝수로 나눠서 계산하는게 맞음.
"""


def solution(n):
    result = 0  
    for length in range(1, n + 1):  # 연속된 숫자의 개수
        if length % 2:  # 홀수 개수
            if n % length == 0 and n // length - length // 2 > 0:
                result += 1
        else:  # 짝수 개수
            if n % length == length // 2 and n // length - length // 2 + 1 > 0:
                result += 1
    return result
