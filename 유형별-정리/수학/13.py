"""

N개의 최소공배수

n개의 최소공배수 구하기.

tip : 여러개의 최소공배수를 동시에 구할 순 없다. 두개씩 구해야함.
tip : 최대공약수는 math.gcd로 구할 수 있고,
최소공배수(lcm)는 a * b // gcd(a, b)로 구할 수 있다.
"""

from math import gcd


def solution(arr):
    Result = arr[0]
    for a in arr[1:]:
        Result = Result * a // gcd(Result, a)
    return Result
