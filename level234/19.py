"""입국심사

각 심사대가 있고
한명당 걸리는 시간이 있는데

비면 다음 사람이 받으면됨.

비었다고 무조건 받지 않아도 됨 근데
왜냐면 끝나는게 오래걸리면 그냥 거기로 안가고
기다렸다가 다른데에서 받는게 더 빠를 수도 있으니깐

어떻게 총 걸리는 시간을 알 수 있을까?
일단 사람은 엄청 많음. 시뮬 불가

분 단위로 시뮬도 물가.

7 * n
10 * m

일단 다 고르게 만들어야함.
n을 어떻게 쪼갤것인가

진짜 모르겟음

이게 이분탐색이구나

모르겠으니깐 정답을 이분탐색으로 추측해나가는거임.

왜냐면 거꾸로 추론이 가능하니깐.

이건 딱 리밋을 정하면 안에 몇명이 들어가는지가 결정됨 1대1로
나이스 하다는 거죠

흠.. 그 코테에서의 문제도 이런식으로 풀 수 있었으려나?
신기하네요 암튼
"""


def solution(n, times):
    left = 0
    right = 10**18

    result = 0

    while left <= right:
        mid = (left + right) // 2

        people = 0
        for time in times:
            people += mid // time

            if people > n:
                break

        if people < n:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    return result
