"""

연속된 부분 수열의 합

비내림차순으로 정렬됨.

부분수열 -> 연속적이여야함. 합은 k
그중에서 길이가 가장 짧은 애. & 가장 앞에 있는 애

답 : [시작인덱스, 끝인덱스]

길이 10^6 -> nlogn까지

그냥 무작정 다 더한다?
그냥 투포인터 쓰면 되는거 아닌가?
투포인터에다가...
min_heap 까지 갈 필요도 없이 그냥 if
"""


def solution(seq, k):
    def is_max(begin_i, end_i):
        if end_i - begin_i < answer[1] - answer[0]:
            return True
        elif end_i - begin_i == answer[1] - answer[0]:
            return begin_i < answer[0]

        return False

    begin_i = 0
    answer = (0, 10**6)
    Sum = 0

    for end_i in range(len(seq)):
        Sum += seq[end_i]

        while Sum > k:
            Sum -= seq[begin_i]
            begin_i += 1

        if Sum == k and is_max(begin_i, end_i):
            answer = (begin_i, end_i)

    return list(answer)


# AI 솔루션
def solution2(seq, k):
    def is_better_subarray(begin_i, end_i):
        # 현재 부분 배열이 더 짧거나, 길이가 같고 시작 인덱스가 더 작은 경우
        current_length = end_i - begin_i
        best_length = answer[1] - answer[0]
        if current_length < best_length:
            return True
        elif current_length == best_length:
            return begin_i < answer[0]
        return False

    begin_i = 0
    answer = (0, 10**6)
    current_sum = 0

    for end_i in range(len(seq)):
        current_sum += seq[end_i]

        # 현재 합이 k를 초과하면, begin_i를 증가시켜 합을 줄임
        while current_sum > k:
            current_sum -= seq[begin_i]
            begin_i += 1

        # 현재 합이 k와 같고, 더 나은 부분 배열이면 갱신
        if current_sum == k and is_better_subarray(begin_i, end_i):
            answer = (begin_i, end_i)

    return list(answer)
