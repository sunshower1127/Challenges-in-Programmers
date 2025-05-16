"""파괴되지 않은 건물

10^6 * 10^5 = 10^11

하나하나 시뮬레이션하면 시간초과인듯?

흠...
어찌됐던 근데 1이상인지 아닌지만 판단하면 되는건데

누적합이라는 기법이라네요
노션에 정리해놨음.
"""

def solution(board, skills):
    height = len(board)
    width = len(board[0])
    temp = [[0] * (width + 1) for _ in range(height + 1)]
    
    for skill in skills:
        skill_type, y1, x1, y2, x2, degree = skill
        amount = (1 if skill_type == 2 else -1) * degree
        temp[y1][x1] += amount
        temp[y2+1][x2+1] += amount
        temp[y1][x2+1] -= amount
        temp[y2+1][x1] -= amount
    
    # 행 기준 누적합
    for y in range(height + 1):
        for x in range(1, width + 1):
            temp[y][x] += temp[y][x-1]
    
    # 열 기준 누적합
    for x in range(width + 1):
        for y in range(1, height + 1):
            temp[y][x] += temp[y-1][x]
    
    # 파괴되지 않은 건물 수 계산
    not_destroyed = 0
    
    for y in range(height):
        for x in range(width):
            board[y][x] += temp[y][x]
            if board[y][x] > 0:
                not_destroyed += 1
    
    return not_destroyed
