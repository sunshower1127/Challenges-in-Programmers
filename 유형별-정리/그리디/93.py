"""광물 캐기

곡괭이가 종류별로 있고
캐야할 광석들이 있음.
근데 연속해서 캐야함. 중간에 킵할 수 없음.

5개캐면 끝남. 최소한의 피로도로...

중요한건 그냥 최대한 높은애를 깨면 되잖아
라는거죠
높은애라는게 곡괭이마다 다를 수 있는데
중요한건 그냥 다이아몬드는 무조건 높은 곡괭이로 캐야한다는거임.
그런식으로 다 되어있음.
그래서 다이아를 25, 철을 5, 돌을 1로 하고 그냥 더한 수가 제일 큰거부터 캐면 됨.

어떤 배열을
다른 배열을 기준으로
정렬하기?
그냥 namedtuple쓰는게 제일 시맨틱한듯.

zip은 inner로 작동함. outer로 작동하게 하려면
"""

from collections import namedtuple


def solution(picks, minerals):
    minerals = minerals[: sum(picks) * 5]

    mineral_list = []
    score = {"diamond": 25, "iron": 5, "stone": 1}
    Mineral = namedtuple("Mineral", "weight minerals")
    for i in range(0, len(minerals), 5):
        mineral_list.append(
            Mineral(
                weight=sum(score[mineral] for mineral in minerals[i : i + 5]),
                minerals=minerals[i : i + 5],
            )
        )

    mineral_list.sort(reverse=True, key=lambda x: x.weight)

    fatigue = {
        "diamond": {"diamond": 1, "iron": 1, "stone": 1},
        "iron": {"diamond": 5, "iron": 1, "stone": 1},
        "stone": {"diamond": 25, "iron": 5, "stone": 1},
    }

    new_picks = ["diamond"] * picks[0] + ["iron"] * picks[1] + ["stone"] * picks[2]

    total_fatigue = 0

    for pick, mineral_data in zip(new_picks, mineral_list):
        total_fatigue += sum(
            fatigue[pick][mineral] for mineral in mineral_data.minerals
        )

    return total_fatigue
