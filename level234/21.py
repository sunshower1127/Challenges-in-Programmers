"""연속 펄스 부분 수열의 합

길이 제한은 없구요
더했다 뺐다 해서 최대값을 return하면 됨.

전형적인 dp 문제죠

그냥 어차피 -한거니깐
마지막에만 - 해주면 되지 않나

자신을 포함해야함

dp 다 까먹어버렸네오 그냥



"""


def solution(sequence):
    N = len(sequence)
    sequence = [num if i % 2 == 0 else -num for i, num in enumerate(sequence)]
    max_dp = [-float("inf")] * (N + 1)
    min_dp = [float("inf")] * (N + 1)

    for n in range(1, N + 1):
        cur = sequence[n - 1]
        max_dp[n] = max(0, max_dp[n - 1]) + cur
        min_dp[n] = min(0, min_dp[n - 1]) + cur

    return max(max(max_dp), -min(min_dp))
