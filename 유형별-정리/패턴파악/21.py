"""n^2 배열 자르기

이건 행렬문제네요 그냥

1은 0,0
2는 0,1 1,0 1,1
3은 0,2 1,2 2,2 2,1 2,0

음... 더하기? 가 아니라
그냥 둘중 큰쪽 + 1 하면 되는거 같은데

이건 패턴파악 문제네요 ㅇㅇ

잠만.
좌표는 어떻게 알아내지
divmod로 알아내지 뭐
- - -
- - -
- - -

"""


def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        y, x = divmod(i, n)
        result.append(max(y, x) + 1)

    return result
