"""최솟값 만들기

A = [1, 4, 2]
B = [5, 4, 4]

서로 곱한값이 최소가 되도록.
생각해봤을때는 가장 큰걸 가장 작은값하고 곱해나가면 되지 않을까?
싶은데
확실하진 않고
이게 그리디지

"""


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))
