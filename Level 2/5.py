"""

이진 변환 반복하기

이진수에서 0을 모두 제거하고, 이진수의 길이를 이진수로 변환 하는게 한단계. 이걸 반복해서 1을 만듦.
"0111010" -> "1111" -> "100"

답 : [반복횟수, 총 제거된 0 개수]

"""


def solution(s):
    cnt_while = 0
    cnt_count = 0
    while s != "1":
        cnt_while += 1
        cnt_count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

    return [cnt_while, cnt_count]
