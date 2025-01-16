"""N-Queen

dfs라고 꼭 재귀함수를 써야하는건 아니다.
충분히 반복문으로도 풀 수 있다.
"""


def solution(n):
    cnt = 0
    path = []

    def dfs():
        nonlocal cnt
        y = len(path)
        if y == n:
            cnt += 1
            return

        for x in range(n):
            if x in path:
                continue
            if any(x - path[i] in [y - i, i - y] for i in range(y)):
                continue
            path.append(x)
            dfs()
            path.pop()

    dfs()
    return cnt


def 반복문solution(n):
    count = 0
    stack = [(-1, [])]  # 초기 상태: (현재 행, 현재까지의 queen 위치 리스트)

    while stack:
        current_row, path = stack.pop()

        if current_row == n - 1:
            count += 1
            continue

        next_row = current_row + 1
        for col in range(n):
            # 현재 열이 유효한지 확인
            conflict = False
            for r, c in enumerate(path):
                if c == col or abs(col - c) == abs(next_row - r):
                    conflict = True
                    break
            if not conflict:
                # 다음 행에 queen을 놓을 수 있으면 스택에 추가
                stack.append((next_row, [*path, col]))

    return count
