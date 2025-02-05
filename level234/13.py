"""불량 사용자

어 문자열에서 와일드카드라.. 인터레스팅이네요

어떻게 해야하지

uid는 8개
라네요

그냥 브루트

dfs?

탐색을 막 해서

user_id가 banned_id에 매칭이 되면
해당 banned_id는 삭제를 하고?
그런식인가?
banned_id를 중심으로 탐색을 하고

음... compile을 하고 여러번 match를 사용하니깐
뭔가 특정 케이스에서 실패가 나오네요
왜지?
이해가 안되긴한데
암튼 조심하자.

"""

import re


def solution(user_id, banned_id):
    result = set()
    unvisited = set(user_id)

    def dfs(n):
        if n == len(banned_id):
            visited = {*user_id} - unvisited
            result.add(tuple(uid for uid in sorted(visited)))
            return

        bid = banned_id[n]
        pattern = re.compile(bid.replace("*", "."))

        for uid in unvisited:
            if len(bid) != len(uid):
                continue
            if not pattern.match(uid):
                continue

            unvisited.remove(uid)
            dfs(n + 1)
            unvisited.add(uid)

    dfs(0)

    return len(result)


def solution2(user_id, banned_id):
    result = set()
    unvisited = set(user_id)
    patterns = [re.compile("^" + bid.replace("*", ".") + "$") for bid in banned_id]

    def dfs(n):
        if n == len(banned_id):
            visited = {*user_id} - unvisited
            result.add(tuple(sorted(visited)))
            return

        for uid in unvisited:
            if len(banned_id[n]) != len(uid):
                continue
            if not patterns[n].match(uid):
                continue

            unvisited.remove(uid)
            dfs(n + 1)
            unvisited.add(uid)

    dfs(0)

    return len(result)
