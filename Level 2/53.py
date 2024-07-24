"""

가장 큰 수

6, 10,2 라면 6210 으로 가장 큰 수 만들기.

처음엔 빈자리에 A를 채워넣어서 정렬하면 될거라고 생각했는데, 아니였음.
숫자가 나열되는건 반복되는것이기때문에 *3을 하는게 맞음.

tip : 다른 배열을 기준으로 정렬할때는 zip하고 정렬한 후 zip(* )을 쓰면 됨.
tip : 머릿속에서 복잡한 함수 쥐어짜내는것보다
    그냥 for if 도배로 구현하는게 더 빠를 수 있음.

"""


# def SortBy(List, Key):
#     Sorted = sorted(zip(Key, List), reverse=True)
#     return list(zip(*Sorted))[1]


def solution(nums):
    nums = sorted(map(str, nums), key=lambda x: x * 3, reverse=True)
    if nums[0] == "0":
        return "0"
    return "".join(nums)
