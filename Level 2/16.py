"""

영어 끝말잇기

n명이서 끝말잇기를 함. 탈락하는 사람의 [번호, 차례] 반환 (없으면 [0, 0])

tip : 원형으로 진행되면, 차례를 구하는건 divmod를 사용하면 된다.

"""


def solution(n, words):
    last = words[0][-1]
    set1 = set([words[0]])
    for i in range(1, len(words)):
        if words[i][0] != last or words[i] in set1:
            q, r = divmod(i, n)
            return [r + 1, q + 1]

        set1.add(words[i])
        last = words[i][-1]

    return [0, 0]
