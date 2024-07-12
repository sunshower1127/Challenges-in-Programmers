"""

주차 요금 계산

fees = 기본시간, 기본요금, 단위시간, 단위요금

record = "시간 차량번호 IN(or OUT)"

IN 했는데 OUT이 없으면 23:59에 OUT 했다고 여김

초과한 시간은 올림해서 단위시간으로 계산

차량번호가 작은 순으로 정렬해서 주차요금 리스트 반환


차량이 IN하면 dict에 {차량 번호 : 출입시간}
넣고
OUT하면 dict에서 꺼내서 계산하면 되겠구만 

enumerate로 쓰고 안쓴다 -> 그냥 이걸로 하자 모르겠으면.

in으로 하고 i가 필요하면 enumerate를 단다

range로 하고 그냥 []로 접근한다
"""

from math import ceil


def TimeConvert(Str):
    H, M = map(int, Str.split(":"))

    return H * 60 + M


def solution(fees, records):
    Sum = dict()
    InTime = dict()
    for Line in records:
        Time, Num, IO = Line.split(" ")
        Time = TimeConvert(Time)

        if IO == "IN":
            InTime[Num] = Time
        else:  # OUT
            if Num not in Sum:
                Sum[Num] = 0

            Sum[Num] += Time - InTime[Num]

            del InTime[Num]

    for Num, Time in InTime.items():
        if Num not in Sum:
            Sum[Num] = 0

        Sum[Num] += TimeConvert("23:59") - Time

    Result = dict()
    for Num, DT in Sum.items():
        Result[Num] = fees[1]

        if DT > fees[0]:
            Result[Num] += ceil((DT - fees[0]) / fees[2]) * fees[3]

    return [Each[1] for Each in sorted(Result.items(), key=lambda x: x[0])]
