"""전화번호 목록

subset인데 이제 접두해야함.

정렬을 할거 같은데 일단

1
12
123

이건 문자열 쪽으로 가야할듯
"""


def solution(phone_book):
    phone_book.sort()
    return all(
        not phone_book[i].startswith(phone_book[i - 1])
        for i in range(1, len(phone_book))
    )
