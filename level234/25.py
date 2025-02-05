"""다단계 칫솔 판매

enroll
referral

seller
amount

트리를 만들어보자.
그냥 작은 규모라서 dict를 써도 될듯
parent만 체크하면 그게 트리지 뭐

수익의 10%를 추천인에게 주는거임.
재귀적으로 반복.

맞네...
이게 계속 %롤 가다보니깐
합쳐서 계산하는거하고
따로 계산하는거하고
차이가 생길 수 있음.
"""

from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = {e: r for e, r in zip(enroll, referral) if r != "-"}

    earn = defaultdict(int)

    for name, cnt in zip(seller, amount):
        cur_name = name  # young
        cur_price = cnt * 100  # 1200

        while True:
            shared = int(0.1 * cur_price)  # 120

            earn[cur_name] += cur_price - shared

            if shared < 1:
                break

            if cur_name not in parent:
                break

            cur_name = parent[cur_name]
            cur_price = shared

    return [earn[name] for name in enroll]
