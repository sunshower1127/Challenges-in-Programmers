"""이진 변환 반복하기

이진수에서 0을 모두 제거하고, 이진수의 길이를 이진수로 변환 하는게 한단계.
이걸 반복해서 1을 만듦.
"0111010" -> "1111" -> "100"

답 : [반복횟수, 총 제거된 0 개수]

너무 쉬워서 안풀겠음

"""


def solution(s):
    WhileCnt = 0
    CountCnt = 0
    while s != "1":
        WhileCnt += 1
        CountCnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

    return [WhileCnt, CountCnt]
