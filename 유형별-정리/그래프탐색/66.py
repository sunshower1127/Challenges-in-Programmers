"""

메뉴 리뉴얼(카카오)

손님이 단품 메뉴를 시킴.(2개이상)

그래서 2명 이상의 손님에게 받은 메뉴조합을 세트메뉴로 낼거임.

주문은 20개. 하나당 길이는 10. 메뉴 개수는 알파벳 개수-> 26?

course에는 이제 메뉴 길이가 들어있고, -> 같은 메뉴길이에 주문 개수가 동일하면 그냥 다 집어넣기.

result에 사전순 오름차순 정렬해서 리턴.

어찌됐던 nCk를 해야됨. -> 10C5 -> 2927  = 36 7 = 252 * 20 = 500정도
nCk 어떻게 만듦? 어... nCk = 이게 아니지 나는 경우의 수를 만들어야하는데
그냥 노가다 하면 될듯.

"""


def solution(orders, course):
    path = ""
    cnt_dict = {}

    def dfs(arr, start, n):
        nonlocal path, cnt_dict
        if n == 0:
            if path not in cnt_dict:
                cnt_dict[path] = 0
            cnt_dict[path] += 1
            return

        for i in range(start, len(arr) - n + 1):
            path += arr[i]
            dfs(arr, i + 1, n - 1)
            path = path[:-1]
        ##

    result = []

    for n in range(len(course)):
        for order in orders:
            dfs(sorted(order), 0, course[n])

        it = sorted(cnt_dict.items(), reverse=True, key=lambda x: x[1])
        for i, (k, v) in enumerate(it):
            if i == 0:
                if v == 1:
                    break
                max_v = v
            elif v != max_v:
                break
            result.append(k)
            ##

        cnt_dict = {}
        ##

    result.sort()
    return result
