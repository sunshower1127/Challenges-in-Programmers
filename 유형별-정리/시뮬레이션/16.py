"""영어 끝말잇기

n명이서 끝말잇기를 함. 탈락하는 사람의 [번호, 차례] 반환 (없으면 [0, 0])

tip : 원형으로 진행되면, 차례를 구하는건 divmod를 사용하면 된다.

"""


def solution(n, words):
    Last = words[0][-1]
    Set = {words[0]}
    for i in range(1, len(words)):
        if words[i][0] != Last or words[i] in Set:
            q, r = divmod(i, n)
            return [r + 1, q + 1]

        Set.add(words[i])
        Last = words[i][-1]

    return [0, 0]
