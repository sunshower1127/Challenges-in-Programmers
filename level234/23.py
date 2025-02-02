"""디스크 컨트롤러

우선순위 큐인데

1. 짧게 걸리는거
2. 빨리 시작한거
3. 작업 번호가 작은거 (인덱스가 작은거)

중간에 끊지않음.

라고 했을때

프로세스에서 실행해달라고 요청한 시간으로부터 실제로 끝나는 시간까지 얼마나 걸렸는지를
평균을 내고 그거의 정수만 따서 출력

실제로 시뮬레이션을 돌려보는게 맞겠죠

흠.. 파이썬이 이게 문제야
튜플을 쓰면 인덱스로 접근해야해서 가독성이 떨어짐.
근데 namedtuple쓰기엔 너무 귀찮아
"""

from collections import deque
from heapq import heappop, heappush


def add_processes(heap, queue, time):
    while queue and queue[0][0] == time:
        start, i, duration = queue.popleft()
        heappush(heap, (duration, start, i))


def solution(jobs):
    jobs = deque(
        sorted((start, i, duration) for i, (start, duration) in enumerate(jobs))
    )
    min_heap = []  # (duration, start, i)
    cur_process = None
    result = []
    for time in range(1000000):
        if not cur_process and not jobs and not min_heap:
            break

        add_processes(min_heap, jobs, time)
        # 프로세스 종료
        if cur_process and time == cur_process[3]:
            result.append(time - cur_process[1])
            cur_process = None

        # 프로세스 선택 및 실행
        if not cur_process and min_heap:
            duration, start, i = heappop(min_heap)
            end = time + duration
            cur_process = (duration, start, i, end)

    return int(sum(result) // len(result))
