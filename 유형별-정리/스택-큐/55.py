"""

다리를 지나는 트럭

트럭n대를 올릴 수 있음. 무게합이 초과하지않고 다 옮겨야함.

2개도 아니고 n개네

시뮬레이션이니깐 완전탐색까진 아닌거같고..

모르겟음

아 정해진 순이네
그럼 그냥 큐 쓰면 될듯.

대기트럭에서 계속 빼내고 -> truck_i

문제읽고 키워드들 대충 주석에 나열해주고
바로 설계 들어가주는데, 코드에서 대충 들어가줌.
변수 이름이나 복잡한 구현에 집착하지말고 대충 설계해주면서
계속 바꿔주면서 머릿속으로 시뮬레이션 돌려주면 됨.
이렇게 풀면 되겠다! 싶으면 바로 구현들어가면 됨.
"""

from collections import deque

MAX = 10**8


def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    bridge_q = deque([0] * bridge_length)
    truck_i = 0
    weight_sum = 0
    for t in range(MAX):
        weight_sum -= bridge_q.pop()
        bridge_q.appendleft(0)

        if truck_i < N and weight_sum + truck_weights[truck_i] <= weight:
            bridge_q[0] = truck_weights[truck_i]
            weight_sum += bridge_q[0]
            truck_i += 1

        elif truck_i == N and weight_sum == 0:
            return t + 1
