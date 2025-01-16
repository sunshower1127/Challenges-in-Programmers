"""[3차] 압축

LZW

A부터 Z까지 다 넣고

이게 왜 그래프 탐색임 근데
이건 그냥 구현인데

"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solution(msg):
    dictionary = ["", *list(ALPHABET)]
    result = []
    index = 0

    while index < len(msg):
        for i, word in reversed(list(enumerate(dictionary))):
            word_len = len(word)
            if msg[index : index + word_len] == word:
                result.append(i)
                dictionary.append(msg[index : index + word_len + 1])
                index += word_len
                break

    return result
