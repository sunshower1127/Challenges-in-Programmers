"""

[3차] n진수 게임

0 1 2 3 ... 9 1 0 1 1 ...

이런식으로 사람들이 돌아가면서 말하는데, 이걸 n진수로 함.

총 m명이고, 자신은 p번째 사람임.

그랬을때 자신이 말하게 될 숫자를 t개 구하면 됨.

11진수 이상부터는 대문자 알파벳으로 표기.

복잡도는 고려하지 않아도 될만큼 작아서
그냥 문자열로 펼쳐놓고 indexing하면 됨.

"""


def solution(n, t, m, p):
    Nums = "0123456789ABCDEF"
    # m*t 만큼 길이의 수열 나열.
    Result = ""
    Idx = 0
    for i in range(m * t):
        if len(Result) == m * t:
            break
        # 진수변환

        Num = ""
        while True:
            q, r = divmod(i, n)
            Num += Nums[r]
            if q == 0:
                break
            i = q

        Result += Num[::-1]
    return "".join(Result[i] for i in range(p - 1, m * t, m))
