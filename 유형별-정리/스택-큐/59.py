"""
큰 수 만들기

number에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 문자열 형태로 return

예) 1924, 2 -> 94
---

문자열 순서는 지켜야함.

큰 숫자 -> 앞자리만 제일 큰걸 계속 뽑아가면 됨. -> 그리디

stack은 list로 구현하는게 deque로 구현하는것보다 나음. 어차피 단반향이니깐..
deque는 queue에만 쓰도록 하자.

이문제는 이제 다 처리했는데 k가 남을 수 있음 -> 그래서 마지막에 정리해줘야함.

tip: while 바깥의 if랑 안쪽의 if는 while 자체의 조건문으로 합칠 수 있음.
"""


def solution(nums, k):
    stack = []
    for num in nums:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # k가 남아있는 경우, 뒤에서부터 k개를 제거
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)
