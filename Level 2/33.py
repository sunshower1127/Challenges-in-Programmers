"""

k진수에서 소수 개수 구하기

n이라는 숫자를 k진수로 바꿈

그 바꾼 숫자에서 0으로 쪼갰을때 10진수 소수가 몇개인지 구하기.

예)
437674 3 -> 211020101011 -> 211 2 1 1 11 -> 소수 3개

진수 변환 -> divmod 쓰면서 2진수부터 계산해보면 금방 알고리즘 만들 수 있음.

소수 판별 -> 그냥 2부터 n**0.5까지 나눠보기 -> 한 번 할 때마다 O(루트n)
dp사용해서 에라토스테네스체(역발상)로 소수 저장해놨다가 갖다 쓰기
-> 세팅하는데 O(nloglogn)-> O(~n) 이고, 판별할때는 당연히 O(1)

이 문제는 10^6 부근이라서 최대 뭐 10^6 나와서 dp 안써도 됨.

"""


def solution(n, k):
    Num = ""
    while True:
        n, r = divmod(n, k)
        Num += str(r)
        if n == 0:
            break

    Num = Num[::-1]

    Cnt = 0
    for Word in Num.split("0"):
        if not Word:
            continue

        n = int(Word)
        Prime = True
        if n == 1:
            Prime = False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                Prime = False
                break

        if Prime:
            Cnt += 1

    return Cnt
