"""서버 증설 횟수

그냥 하면 되는거 같은데
딱히 뭐 알고리즘...
아니 뭐 복잡도도 없고
노가다네요
선입선출이니깐 queue
"""

from collections import deque

def solution(players, m, k):
    server_q = deque() # (시작index, 개수)
    server_size = 0
    server_increment_cnt = 0
    for i, player in enumerate(players):
        # 수명 다한 서버 없애기
        if server_q and i == server_q[0][0] + k:
            server_size -= server_q.popleft()[1]
        
        # 서버 증설하기
        remains = player//m - server_size
        if remains > 0 :
            server_increment_cnt += remains
            server_size += remains
            server_q.append((i, remains))
            
        print(remains)
    
    return server_increment_cnt
        
        
        