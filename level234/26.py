"""[1차] 셔틀버스


09:00부터 n회 t분간격 최대 m명 탑승 가능

막 추가되는데

23:59에 집에 돌아간다라..
맨뒤에 서야함.

최대한 마지막 셔틀을 타야한다 이거죠

그냥 시뮬레이션 돌리면 되는거 아닌가요

라고 하기엔 이제

언제까지 쨀 수 있니

음...

가장 늦은 셔틀 부터 탐색해보는데

예를들면

1명씩 탈 수 있는 셔틀.

그냥 시뮬을 돌리고

마지막 셔틀 상황을 재현하고
그걸 어떻게 탈 수 있는지

쉽지않았네요 구현하기


"""

from collections import deque


def to_mins(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def to_str(mins):
    h, m = divmod(mins, 60)
    return f"{h:02d}:{m:02d}"


def append_crew(line, timetable, cur_time):
    while timetable and timetable[0] <= cur_time:
        line.append(timetable.popleft())


def pop_n(line, n):
    is_over = len(line) < n

    last_value = None

    while line and n > 0:
        last_value = line.popleft()
        n -= 1

    return (is_over, last_value)


def solution(num, between_time, crew_limit, timetable):
    timetable.sort()
    timetable = deque(map(to_mins, timetable))
    line = deque()
    shuttle_time = deque(to_mins("09:00") + between_time * i for i in range(num))

    for cur_time in range(to_mins("09:00"), to_mins("24:00")):  # noqa: RET503
        append_crew(line, timetable, cur_time)

        if cur_time == shuttle_time[0]:
            is_over, last_crew_time = pop_n(line, crew_limit)
            shuttle_time.popleft()

            if not shuttle_time:
                if is_over:
                    return to_str(cur_time)

                return to_str(last_crew_time - 1)  # type: ignore[]
