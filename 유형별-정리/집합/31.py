"""

전화번호 목록

접두어 : 한 문자열이 다른 문자열의 시작 서브셋일 경우.

전화번호가 접두어가 있는경우 False, 아닌경우 True 반환

119는 1195524421의 접두어이다. -> False

전화번호 리스트의 길이가 10^6 -> 시간 복잡도 생각해야함. 정렬은 가능.
정렬은 10^6 까지 가능함. 10^7부터는 불가능.
중복은 없음.
전화번호 길이는 최대 20

-> 정렬을 하자. 문자열 접두어는 정렬하면 바로 보임.

근데 다르게 풀 수도 있음.
문자열의 길이가 최대 20이니깐.
for문을 돌려서 자신의 서브 문자열을 검색하면 됨. -> 존재하는지만 알면 되니깐
set을 씀.

정렬하면 O(nlogn)이고, set을 쓰면 O(n)이다. 10^7이였으면 무조건 set을 썼어야함.
"""


def solution(phone_book):
    Set = set(phone_book)

    for Each in Set:
        for i in range(len(Each) - 1):
            if Each[: i + 1] in Set:
                return False

    return True
