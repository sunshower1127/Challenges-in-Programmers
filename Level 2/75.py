"""
테이블 해쉬 함수

튜플들을 col 값 기준으로 오름차순으로. (같으면 첫번째 컬럼값으로 내림차순.)

S_i = i번째 튜플에서 각 컬럼을 i로 나눈 나머지의 합

row begin ~ end 까지 모든 S_i를 xor한 값이 해쉬값임.

tip1: Iterator는 슬라이스가 안되는데,그때 보통 list화 하는데, `list()`를 쓸건지 `[*]`를 쓸건지 못정함.
tip2: `^`는 xor연산자임.
tip3: enumerate의 2버째 인자로 시작값을 줄 수 있음. 완전 나이스네

근데 list(enumerate(data, 1))[row_begin - 1 : row_end] 이런식으로 할바엔 range 쓰는게 더 깔끔할거 같은데
뭐 그냥 상관 없는거 같습니다.

"""


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    reduced = 0
    for i, row in [*enumerate(data)][row_begin - 1 : row_end]:
        hashed = sum(v % (i + 1) for v in row)
        reduced ^= hashed

    return reduced
