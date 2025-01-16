"""

숫자 나누기

철수
영희

가장 큰 a
철수의 숫자는 모두 나눌 수 있고, 영희는 다 나눌 수 없음
반대도 가능.

10 5 20 17

10 20
5 17
나눠 가지면
a는 10이 됨.

최대공약수하고 최소공배수 문제인거 같은데?
10 20이면 -> 최대공약수가 10이고, 얘의 약수가 a의 후보군이 되고,
5 17의 최대공약수가 1임.
10부터 해본다고 치자.
음!
최대공약수 약수들 - 최소공배수 약수들
하면 되겠는데?
10

한쪽의 최대공약수를 a
다른 한쪽의 최대공약수를 b
a의 약수이면서 b의 배수가 아닌?

합쳐서 배열 길이는 10^6
원소 크기는 10^8
1부터 해보지말라는거죠



"""

import math
from functools import reduce


def solution(arrayA, arrayB):
    gcd_a = reduce(math.gcd, arrayA)
    gcd_b = reduce(math.gcd, arrayB)

    answer1 = answer2 = 0

    for b in arrayB:
        if b % gcd_a == 0:
            break
    else:
        answer1 = gcd_a

    for a in arrayA:
        if a % gcd_b == 0:
            break
    else:
        answer2 = gcd_b

    return max(answer1, answer2)


def get약수(num):
    s = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            s.add(i)
            s.add(num // i)
    return s


# 실패 솔루션 -> 약수는 건들지마 -> 숫자가 너무 큼
def solution_1(arrayA, arrayB):
    gcd = reduce(math.gcd, arrayA)
    lcm = reduce(lambda x, y: (x * y) // math.gcd(x, y), arrayB)

    answer1 = answer2 = 0
    if result := get약수(gcd) - get약수(lcm):
        answer1 = max(result)

    gcd = reduce(math.gcd, arrayB)
    lcm = reduce(lambda x, y: (x * y) // math.gcd(x, y), arrayA)

    if result := get약수(gcd) - get약수(lcm):
        answer2 = max(result)

    return max(answer1, answer2)
