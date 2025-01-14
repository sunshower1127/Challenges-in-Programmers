"""숫자 블록

어우야..

10^9 이고
어 네

i를보고 어떤 블록이 있는지 맞춰야함.
n*2 부터니깐
n/2가 있지 않을까요

짝수 -> n/2가 적형ㅆ고

홀수 -> n/3 ?

근데 3으로 안나눠지면?
5
...
이렇게 소수로 계속 나눠줘야함.


1 2 3 4 5 6 7 8 910
0 1 1 2 1 3 1 4 3 5

소수...

일단 소수 테이블(에라스토테네스의 체?)을 만들 수도 있꼬
직접 계산할 수도 이쓴데

직접 계산부터 해봅시다.

아무것도 안나눠져?

"""


def solution(begin, end):
    result = []
    for num in range(begin, end + 1):
        for i in range(2, int(num**0.5) + 1):
            q, r = divmod(num, i)
            if r == 0 and q <= 10_000_000:
                result.append(i)
                break
        else:  # no break
            result.append(1)

    if begin == 1:
        result[0] = 0
    return result
