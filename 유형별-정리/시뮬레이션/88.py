"""과제 진행하기

말이 과제지 스케쥴러네요

과제 중일때 새로운 과제가 나오면 -> 바로 하던거 킵하고 새로운 과제.
여유가 생기면 멈춰둔 과제를 하는데,  가장 최근에 멈춘것부터 -> 스택이네요

드디어 복잡한 반복문 조건문 잘 풀 수 있네요

tip1: 복잡한 반복문은 for문 대신 while문에다가 i += 1을 쓰자.
tip2: 복잡한 조건문은 < == > 3개 경우로 나누고 각각 주석 붙여서(안붙이면 많이 헤맴) 경우를 처리하면 된다.
"""

NAME = 0
START = 1
DT = 2


def 남는시간활용(wait_stack, complete, remaining):
    while wait_stack:
        name, dt = wait_stack.pop()

        remaining -= dt  # 20분남았는데 30분짜리해야함
        if remaining < 0:
            wait_stack.append((name, -remaining))
            return
        complete.append(name)


def get_min(s):
    h, m = map(int, s.split(":"))
    return 60 * h + m


def solution(plans):
    # 시작 시간 기준으로 정렬하고 (그냥 문자열 채로)

    # 시뮬레이션 돌리면 될듯 하나씩 꺼내면서 다음꺼하고 비교하기.

    wait_stack = []
    complete = []

    plans.sort(key=lambda x: x[1])

    plan_i = 0
    while True:
        name, start, dt = plans[plan_i]
        dt = int(dt)
        if plan_i < len(plans) - 1:
            remaining = get_min(plans[plan_i + 1][START]) - get_min(start)
            # remaining -> 사이 시간. 50분
            # dt -> 해야하는 시간. 30분
            if remaining < dt:
                wait_stack.append((name, dt - remaining))
                plan_i += 1
                continue

            complete.append(name)
            plan_i += 1

            if remaining > dt:
                남는시간활용(wait_stack, complete, remaining - dt)

            continue

        # 마지막 할일인 경우
        complete.append(name)
        if wait_stack:
            complete += reversed(next(zip(*wait_stack)))
        return complete
