"""광물 캐기

이게 브루트포스로도 풀 수 있게 해놨지만
사실은 가중치로도 풀 수 있음.
왜냐면 철 곡괭이로 캘때 보면 다이아가 5임.
5개씩 끊는데 다이아가 5인건 아무리 iron하고 stone이 많아도 다이아 1개를 못이긴다는거임.
즉, 서로 자릿수가 생긴다고 보면 됨. 간섭할 수 없는
그래서 다이아, 철, 돌 순으로 정렬하면 정렬이 되고
그 순으로 그냥 다이아 곡괭이부터 쓰면됨. 그리디.

결국은 그리디 문제였다~

코드 다시 짜긴 그렇고 남의 코드 그냥 빌려씀
"""
# 풀이과정
# 1.곡괭이 수 * 5 만큼의 광석만 캘 수 있으므로 광석의 크기가 더 클경우 자름
# 2.광물을 연속해서 5개를 캐야하므로 5개씩 광물을 잘라서 새로운 배열에 저장한다.
# 3.광물은 주어진 순서대로, 곡괭이는 순서가 상관없으므로 광물을 다이아몬드, 철, 돌 순서대로 정렬한다.
# 4.광물의 갯수만큼 반복하니 시간 복잡도는 O(N)이다.


def solution(picks, minerals):
    answer = 0
    sum = 0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i

    # 곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals) > sum:
        minerals = minerals[:num]

    # 광물들을 조사한다.
    new_minerals = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            new_minerals[i // 5][0] += 1
        elif minerals[i] == "iron":
            new_minerals[i // 5][1] += 1
        elif minerals[i] == "stone":
            new_minerals[i // 5][2] += 1

    # 광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    new_minerals.sort(reverse=True, key=lambda x: (x[0], x[1], x[2]))

    # 정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
        dia, iron, stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * dia) + (5 * iron) + stone
                break

    return answer
