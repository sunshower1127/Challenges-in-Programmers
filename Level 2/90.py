"""이모티콘 할인행사

유저 입장에서 할인율이 몇% 이상인 이모티콘은 무조건 삼

할인율을 점점 올려서 구매하는 이모티콘 가격의 합이 자신이 생각한 리밋보다 높으면 패스를 삼.

할인율을 너무 올리면 가격이 싸져서 패스를 안삼.

암튼 이래서 각각의 이모티콘의 할인율을 어떻게 조정해서 최대한 많은 이모티콘 패스를 구매하게 할지, + 판매액을 늘릴지

일단 사용자 한명에게 집중하면

가격 = sum(price*각각의할인율 for price in emoticons if 각각의할인율 >= 유저할인율)
if 가격 >= 리밋: pass수 += 1

이 비율은 1~40까지고

이모티콘은 7개임. -> 10^2*7 -> 10^14
브루트는 당연히 안되는거고 뭐

아니 브루트 말고는 뭐 안떠오르는데

아 그냥 긴거는 2번 읽어라 아 짜잉나네
10 20 30 40 중 하나라네요 그럼 4**7 -> 2**14 -> 10^6정도니깐 가능

tip: 긴 문제는 여러번 꼼꼼히 읽어라.
"""


def get_sale_ratios(emo_len):
    # return [[30, 40]]
    results = []
    path = []

    def dfs():
        if len(path) == emo_len:
            results.append([*path])
            return

        for sale in (10, 20, 30, 40):
            path.append(sale)
            dfs()
            path.pop()

    dfs()
    return results


def max_record(result, record):
    if result[0] > record[0]:
        return result
    if result[0] == record[0]:
        if result[1] < record[1]:
            return record
        return result
    if result[0] < record[0]:
        return record


def solution(users, emoticons):
    result = [0, 0]
    # 모든 경우의수 가져오기
    emo_len = len(emoticons)
    for sale_ratio in get_sale_ratios(emo_len):
        # 10 20        40 40 20 40
        record = [0, 0]
        for user_sale, user_limit in users:
            total_price = sum(
                price * (100 - sale) // 100
                for price, sale in zip(emoticons, sale_ratio)
                if sale >= user_sale
            )
            if total_price >= user_limit:
                record[0] += 1
            else:
                record[1] += total_price

        result = max_record(result, record)

    return result
