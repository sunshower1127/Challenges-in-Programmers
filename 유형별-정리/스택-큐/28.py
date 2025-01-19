"""프로세스

큐

그냥 뭐.. 큐를 네.

"""

from collections import Counter, deque


def solution(priorities, location):
    counter = Counter(priorities)
    counter = deque(sorted(counter.items(), reverse=True))
    q = deque(priorities)
    time = 0
    while q:
        priority = q.popleft()

        if priority == counter[0][0]:
            counter[0] = (counter[0][0], counter[0][1] - 1)
            if counter[0][1] == 0:
                counter.popleft()

            time += 1

            if location == 0:
                return time

        location -= 1
        q.append(priority)
        if location == -1:
            location += len(q)
