def permutations(arr, r):
    result = []
    visited = [False] * len(arr)

    def backtrack(path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                path.append(arr[i])
                backtrack(path)
                visited[i] = False
                path.pop()

    backtrack([])
    return result


def combinations(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def product(*args, repeat=1):
    """원리가 어떻게 되냐면
    product("ABC", repeat=2)라고 하자,
    그러면 pools = [[ABC], [ABC]]
    result = [[]] -> [A, B, C] 가 되겠죠
    이 다음 pool에서는
    [A, B, C]에 각자 자기들을 뒤에 갖다 붙이면 됨
    [[AA], [AB], [AC], [BA], [BB], [BC], [CA], [CB], [CC]]
    이런식으로 계속 이어 붙이는 거인듯.
    조금 어렵긴한데 뭐 풀다보면 괜찮을듯.
    """
    pools = [list(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        new_result = []
        for path in result:
            for x in pool:
                new_result.append([*path, x])
        result = new_result
    return result
