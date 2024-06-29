"""

튜플

튜플은 중복가능, 순서가 있음. -> 함수 인자를 생각해보자.

"{{2},{2,1},{2,1,3},{2,1,3,4}}"
이 주어지면 (2, 1, 3, 4) 이라는 튜플을 반환하면 됨.

단, 순서가 중요함.
크기가 작은(개수가 작은) 집합의 원소부터 앞으로 와야함.
2 < 2, 1 < 2, 1, 3 < 2, 1, 3, 4
이므로 순서는
2, 1, 3, 4 가 되는거임.

tip : 괄호가 들어이쓴 문자열 해석할때 굳이 복잡하게 안해도 됨. split('},{')
"""


def solution(s):
    List = s[2:-2].split("},{")
    Mat = [set(Each.split(",")) for Each in List]
    Mat.sort(key=lambda x: len(x))

    Result = list(Mat[0])

    for i in range(1, len(Mat)):
        Result.append(tuple(Mat[i] - Mat[i - 1])[0])

    return list(map(int, Result))
