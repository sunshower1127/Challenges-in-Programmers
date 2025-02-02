"""가장 긴 팰린드롬

흠...

dp라고 하면

aabada
abaca

중심부를 잡고,
대칭성인지 판단해나가는게
나는 베스트라고 생각함.
암튼

.5 단위로 인덱스를 잡을 순 없으니깐
dict를 쓰던지 해야할거 같은데

.5단위는 defaultdict로 처리하던가 하자
나이스

"""

from collections import defaultdict


def solution(s):
    N = len(s)
    dp = defaultdict(int)  # 0
    done = defaultdict(bool)  # False

    for n in range(N):
        dp[n] = 1

        for left in range(n):
            mid = (left + n) / 2
            if done[mid]:
                continue

            if s[left] == s[n]:
                dp[mid] += 2
            else:
                done[mid] = True

    return max(dp.values())
