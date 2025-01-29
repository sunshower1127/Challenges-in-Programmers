"""네트워크

몇개예요?

"""


def solution(n, computers):
    visited = 0
    cnt = 0

    for i in range(n):
        if visited == n:
            break
        if 1 << i & visited:
            continue

        stack = [i]
        visited |= 1 << i
        cnt += 1

        while stack:
            node = stack.pop()

            for next_node in range(n):
                if 1 << next_node & visited:
                    continue
                if computers[node][next_node]:
                    stack.append(next_node)
                    visited |= 1 << next_node

    return cnt
