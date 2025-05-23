"""2개 이하로 다른 비트

이런 류 문제 싫어하긴함

패턴 파악해내는건데 코딩 실력보단 뭐랄까
문제적 남자에서 문제푸는거 같아서 싫음.

보니깐 그냥 정직하게 풀어도 되는거 같던데
한 번 봐야겠음 나중에.

"""


def solution(nums):
    result = []
    for num in nums:
        bin_str_arr = list("0" + bin(num)[2:])
        for i in reversed(range(len(bin_str_arr))):
            if bin_str_arr[i] == "0":
                bin_str_arr[i] = "1"
                if i + 1 < len(bin_str_arr):
                    bin_str_arr[i + 1] = "0"
                break

        result.append(int("".join(bin_str_arr), 2))
    return result


"""

Copliot 코드인데 바로 비트연산 사용하는 것임.
어려워서 굳이..

"""


def solution2(nums):
    result = []
    for num in nums:
        if num % 2 == 0:  # 짝수인 경우
            result.append(num + 1)
        else:
            # 홀수인 경우
            lowest_zero_bit = (~num) & (num + 1)  # 가장 낮은 0 비트 찾기
            result.append(num + lowest_zero_bit // 2)
    return result
