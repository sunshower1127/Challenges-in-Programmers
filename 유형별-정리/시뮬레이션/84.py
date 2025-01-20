"""문자열 압축
코드가 길어질 수록 투두 작성은 필수입니다.
뇌가 꼬이는 순간 함수부터 만드는거임 그냥
함수로 퉁친다. 이거거든요
함수 구현은 맨 나중임.
TODO: 이거 한 번 풀어보셈
"""


def 개수대로쪼개기(s, i):
    ls = []
    for j in range(0, len(s), i):
        ls.append(s[j : j + i])
    return ls


def 어디까지같은지(ls, start_idx):
    for i in range(start_idx + 1, len(ls)):
        if ls[start_idx] != ls[i]:
            return i - 1

    return len(ls) - 1


def solution(s):
    min_length = float("INF")
    for i in range(1, len(s) + 1):
        length = 0
        ls = 개수대로쪼개기(s, i)
        # ls = ["a", "b", "c"]
        start_idx = 0
        while start_idx != len(ls):
            end_idx = 어디까지같은지(ls, start_idx)
            cnt = end_idx - start_idx
            if cnt != 0:
                length += len(str(cnt + 1))
            length += len(ls[start_idx])

            start_idx = end_idx + 1

        min_length = min(min_length, length)

    return min_length
