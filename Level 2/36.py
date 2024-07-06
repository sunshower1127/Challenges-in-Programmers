"""

[3차] 압축


LZW 압축 알고리즘이라고 함.

1. 일단 알파벳 한글자 짜리를 모두 사전에 등록
2. 문자열을 순차적으로 읽는데, 사전에서 찾을 수 있는 가장 긴 문자열을 매칭
3. 매칭하면 그것보다 한글자 더 긴 문자열을 사전에 등록

예)
KAKAO

1. K가 알파벳 1글자라 이미 사전에 있으므로 사전의 K index -> 11
2. KA가 사전에 없으므로 사전에 KA 등록 -> 27
3. A가 알파벳 1글자라 이미 사전에 있으므로 사전의 A index -> 1
4. AO가 사전에 없으므로 사전에 AO 등록 -> 28
5. KA가 사전에 있으므로 사전의 KA index -> 27
6. KAO가 사전에 없으므로 사전에 KAO 등록 -> 29
7. O가 알파벳 1글자라 이미 사전에 있으므로 사전의 O index -> 15

결과 : [11, 27, 15, 28, 29]

1000글자 제한
-> 문자열과 index 매칭할때, 문자열->index 검색은 dict를 따로 만드는게 빠르긴함.
근데 1000글자면 굳이 안만들고 list로 해도 될듯. 해봤자 10^6 정도니깐

"""


def solution(msg):
    Dict = {chr(i): i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
    Result = []
    N = len(msg)
    Idx = 0
    while Idx < N:
        Break = False
        for Len in range(1, N - Idx + 1):
            if msg[Idx : Idx + Len] not in Dict:
                Dict[msg[Idx : Idx + Len]] = len(Dict) + 1
                Result.append(Dict[msg[Idx : Idx + Len - 1]])
                Idx += Len - 1
                Break = True
                break

        if not Break:
            Result.append(Dict[msg[Idx : Idx + Len]])
            return Result


# s가 3이고, v가 91임
#
