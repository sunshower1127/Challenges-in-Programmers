"""

[3차] 방금 그곡

시작시간, 종료시간, 음악제목, 악보정보.
반복해서 이어 붙여야함 시간만큼.
그중에서 해당 문자열을 찾으면 반환.
재생시간, 음악제목 순으로 정렬

tip : c++을 제외한 다른 언어에서는 문자열은 readonly이다. 리스트로 바꾸거나 그냥 새로 써야함.

"""


def convert(notes):
    new_notes = []
    for note in notes:
        if note == "#":
            new_notes[-1] = new_notes[-1].lower()
        else:
            new_notes.append(note)

    return "".join(new_notes)


def get_mins(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


def solution(m, musicinfos):
    m = convert(m)
    ls = []
    for info in musicinfos:
        begin_t, end_t, title, notes = info.split(",")
        t = get_mins(end_t) - get_mins(begin_t)
        ls.append((t, title, convert(notes)))

    ls.sort(reverse=True, key=lambda x: x[0])

    for t, title, notes in ls:
        q, r = divmod(t, len(notes))
        notes = notes * q + notes[:r]
        if m in notes:
            return title

    return "(None)"
