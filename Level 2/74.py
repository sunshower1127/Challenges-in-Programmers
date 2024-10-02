"""

수식 최대화 (카카오 인턴)

예측하는건 의미가 없고
연산자 만나면 흠...

연산자 우선순위니깐
줄을 세워야겠죠.

근데 내가 이걸 구현해본적이 없느데
연산자를 찾고(n)
양쪽에 숫자까지 도달하고(n)
계산하고 무한반복

1. 연산자 3개 permu 해서 우선순위 정하기
2. 연산자 문자열 내에서 찾기
3. 순서대로 계산해주기
        a. 왼쪽 숫자, 오른쪽 숫자 구하기
    b. 연산자 적용해서 문자열 교체해주기
4. 절대값인 최댓값 찾아서 답 내놓기

진짜 처음부터 다시 만들거임.
핵심은
1. 테스트
2. 함수화

일단 -가 음수일수도있음(계산하다보면.)

---

여기가 터닝포인트였음.
화
tip1. 사실 permutations 안쓰고 for문 3개 썼어도 쉽게 구현했을듯
    -> 이런쪽에선 카카오가 섬세함.
tip2. -가 음수도 될 수 있기 때문에 예외처리가 쉽지 않았음. 예외처리 -> 무조건 함수화

"""

from itertools import permutations
from pprint import pprint


def find_op(expr, op):
    """
    op를 찾아야하는데, 못찾으면 -1
    중요한 -에 대한 예외가 필요함.
    """

    for i, c in enumerate(expr):
        if c == op:
            if op != "-":
                return i

            if i == 0:
                continue
            if not expr[i - 1].isdigit():
                continue

            return i
        ##
    return -1


def find_left(expr, op_i):
    """
    음수 예외 설정 해야함.
    """
    for i in reversed(range(1, op_i)):
        if expr[i] in ["*", "+"]:
            return i + 1

        elif expr[i] == "-":
            if not expr[i - 1].isdigit():
                return i
            else:
                return i + 1
        ##
    return 0


def find_right(expr, op_i):
    """
    얘도 - 예외 설정해야함.
    """
    for i in range(op_i + 2, len(expr) - 1):
        if not expr[i].isdigit():
            return i - 1

    return len(expr) - 1


def get_value(expr, ops):
    for op in ops:
        while (op_i := find_op(expr, op)) != -1:
            left_i = find_left(expr, op_i)
            right_i = find_right(expr, op_i)
            # -> 123 + 456 이면 1의 i가 left_i, 6의 i가 right_i

            left_num = int(expr[left_i:op_i])
            right_num = int(expr[op_i + 1 : right_i + 1])

            if op == "+":
                result = left_num + right_num
            elif op == "-":
                result = left_num - right_num
            else:
                result = left_num * right_num

            expr = f"{expr[:left_i]}{result}{expr[right_i+1:]}"

        # while
    # for
    return int(expr)


def solution(expr):
    per = permutations("-+*")
    max_v = 0
    for ops in per:
        max_v = max(max_v, abs(get_value(expr, ops)))

    return max_v
