"""

n^2 배열 자르기

1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4

이런 n x n 배열을 행으로 잘라내서 가로로 이어붙여서 1차원 배열로 만들고
arr[left:right+1] 구하기

tip : n이 10^7이라서 진짜로 2차원 배열 만들면 메모리 초과임. 10^14임
    -> left하고 right을 2차원으로 변환하는게 맞다.
"""


def solution(n, left, right):
    return [max(divmod(i, n)) + 1 for i in range(left, right + 1)]
