"""이진 변환 반복하기

이진수에서 0을 모두 제거하고, 이진수의 길이를 이진수로 변환 하는게 한단계.
이걸 반복해서 1을 만듦.
"0111010" -> "1111" -> "100"

답 : [반복횟수, 총 제거된 0 개수]

이게 10진수에서 2진수 변환은 파이썬에서 bin()을 지원해주는데
뭐 3진수라던지 바리에이션이 나올 수도 있으니깐 직접 구현하는게 좋을 수 있음.

"""


def dec_to_bin(dec):
    result = []
    q = dec
    while True:
        if q == 0: break
        q, r = divmod(q, 2)
        result.append(str(r))
    
    return "".join(reversed(result))

def solution(s):
    cnt = 0
    removed_zero_cnt = 0
    while True:
        if s == "1":
            return [cnt, removed_zero_cnt]
        
        length = len(s)
        s = s.replace("0", "")
        new_length = len(s)
        removed_zero_cnt += length - new_length
        
        s = dec_to_bin(new_length)
        
        cnt += 1
        