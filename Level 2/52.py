"""

2개 이하로 다른 비트

이런 류 문제 싫어하긴함

패턴 파악해내는건데 코딩 실력보단 뭐랄까
문제적 남자에서 문제푸는거 같아서 싫음.

보니깐 그냥 정직하게 풀어도 되는거 같던데
한 번 봐야겠음 나중에.

"""


def solution(Nums):
    Result = []
    for Num in Nums:
        Str = list("0" + bin(Num)[2:])
        for i in reversed(range(len(Str))):
            if Str[i] == "0":
                Str[i] = "1"
                if i + 1 < len(Str):
                    Str[i + 1] = "0"
                break

        Result.append(int("".join(Str), 2))
    return Result
