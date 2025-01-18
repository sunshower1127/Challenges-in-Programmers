"""[3차] 방금그곡

음악 제목, 재생시간, 끝난시간, 악보
1분에 한개씩
음악은 무한 반복

여러개면 제목이 재생시간이 제일 긴애. -> 도 똑같으면 그냥 먼저 입력된애

없으면 "(None)"

musicinfo
시작시간 끝난시간 제목, 음

흠. 일단 m이 music보다 긴경우 -> music을 쭉 이어야함
m이 music보다 작은경우 -> 매칭하면 됨.

"""

import re
from collections import namedtuple


def get_note_list(notes):
    return re.findall(r"[A-Z]#?", notes)


def get_total_mins(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(m, musicinfos):
    answers = []
    Answer = namedtuple("Answer", "title duration")

    neo_music = f" {' '.join(get_note_list(m))} "
    for musicinfo in musicinfos:
        time_start, time_end, title, notes = musicinfo.split(",")
        duration = get_total_mins(time_end) - get_total_mins(
            time_start
        )  # 음수일 가능성? X
        note_list = get_note_list(notes)
        note_list *= (duration // len(note_list)) + 1
        note_list = note_list[:duration]
        music = f" {' '.join(note_list)} "

        if neo_music in music:
            answers.append(Answer(title, duration))

    if not answers:
        return "(None)"

    answers.sort(reverse=True, key=lambda v: v.duration)

    return answers[0].title
