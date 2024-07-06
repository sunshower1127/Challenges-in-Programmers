"""

모음사전

AEIOU 로 이루어진 사전임.
근데 이 사전은 순서가 다르다.

A
AA
AAA
AAAA
AAAAA
AAAAE
AAAAI
AAAAO
AAAAU
AAAE


이런 순서임.

word의 순서를 알아내면 되는데, 워드의 최대 길이는 5임

길이가 5니깐 굳이 시간복잡도 생각을 안해도 됨.

보면 패턴이 재귀함수랄까 for문도 가능하겠고
그냥 for문 5개 써서 list 만들고 find 하는게 빠르겠네요.

아래 풀이는 시간 엄청 들여서 찾은 수학 계산인데
만약 시간복잡도가 높아보인다면 이걸 쓰면 되겠지만
이 문제는 그런 문제가 아니죠...

"""


def solution(word):
    Num = 0

    Len = len(word)

    Num += Len

    Str = "AEIOU"

    Tuple = (781, 156, 31, 6, 1)
    for i in range(Len):
        Num += Str.find(word[i]) * Tuple[i]

    return Num
