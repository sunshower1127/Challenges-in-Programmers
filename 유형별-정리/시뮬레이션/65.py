"""호텔 대실

흠.
1000개.
하루를 분으로 계산하면 -> 24 * 60 = 1440분 ->
1000000 -> 10^6 -> EZ

"""


def 시간변환(Str):
    h, m = map(int, Str.split(":"))
    return h * 60 + m


def solution(book_time):
    cnt_list = [0] * (24 * 60 + 11)

    for b, e in book_time:
        for i in range(시간변환(b), 시간변환(e) + 10):
            cnt_list[i] += 1

    return max(cnt_list)


def convert_time(Str):
    h, m = map(int, Str.split(":"))
    return h * 60 + m


def solution2(book_time):
    time_slots = [0] * (24 * 60 + 11)

    for b, e in book_time:
        for i in range(convert_time(b), convert_time(e) + 10):
            time_slots[i] += 1

    return max(time_slots)
