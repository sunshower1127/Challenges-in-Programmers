"""지게차와 크레인

A 회사의 물류창고에는 알파벳 대문자로 종류를 구분하는 컨테이너가 세로로 n 줄, 가로로 m줄 총 n x m개 놓여 있습니다. 특정 종류 컨테이너의 출고 요청이 들어올 때마다 지게차로 창고에서 접근이 가능한 해당 종류의 컨테이너를 모두 꺼냅니다. 접근이 가능한 컨테이너란 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너를 말합니다.

최근 이 물류 창고에서 창고 외부와 연결되지 않은 컨테이너도 꺼낼 수 있도록 크레인을 도입했습니다. 크레인을 사용하면 요청된 종류의 모든 컨테이너를 꺼냅니다.

물류창고-1-1.drawio.png

위 그림처럼 세로로 4줄, 가로로 5줄이 놓인 창고를 예로 들어보겠습니다. 이때 "A", "BB", "A" 순서대로 해당 종류의 컨테이너 출고 요청이 들어왔다고 가정하겠습니다. “A”처럼 알파벳 하나로만 출고 요청이 들어올 경우 지게차를 사용해 출고 요청이 들어온 순간 접근 가능한 컨테이너를 꺼냅니다. "BB"처럼 같은 알파벳이 두 번 반복된 경우는 크레인을 사용해 요청된 종류의 모든 컨테이너를 꺼냅니다.

물류창고-1-2.drawio.png

위 그림처럼 컨테이너가 꺼내져 3번의 출고 요청 이후 남은 컨테이너는 11개입니다. 두 번째 요청은 크레인을 활용해 모든 B 컨테이너를 꺼냈음을 유의해 주세요. 세 번째 요청이 들어왔을 때 2행 2열의 A 컨테이너만 접근이 가능하고 2행 3열의 A 컨테이너는 접근이 불가능했음을 유의해 주세요.

처음 물류창고에 놓인 컨테이너의 정보를 담은 1차원 문자열 배열 storage와 출고할 컨테이너의 종류와 출고방법을 요청 순서대로 담은 1차원 문자열 배열 requests가 매개변수로 주어집니다. 이때 모든 요청을 순서대로 완료한 후 남은 컨테이너의 수를 return 하도록 solution 함수를 완성해 주세요.
"""


"""지게차와 크레인

재밌네
모든 바깥쪽 블럭들을 계속 메모리에 넣고 갱신해야줘야함.
dfs가 어떻게 되는거야
패딩을 넣어줍시다.
"""

def pick_boundary(y, x, storage, target, isEmpty, height, width, visited):
    if not (0<=y<height+2 and 0<=x<width+2 and (y, x) not in visited):
        return
    
    visited.add((y, x))
    
    if isEmpty[y][x]:
        pick_boundary(y+1, x, storage, target, isEmpty, height, width, visited)
        pick_boundary(y-1, x, storage, target, isEmpty, height, width, visited)
        pick_boundary(y, x+1, storage, target, isEmpty, height, width, visited)
        pick_boundary(y, x-1, storage, target, isEmpty, height, width, visited)
        return    
    
    if storage[y-1][x-1] == target:
        isEmpty[y][x] = True

def solution(storage, requests):
    height = len(storage)
    width = len(storage[0])
    
    isEmpty = [[False] * (width+2) for _ in range(height+2)]
    for y in (0, height+1):
        for x in range(0, width+2):
            isEmpty[y][x] = True
    
    for x in (0, width+1):
        for y in range(0, height+2):
            isEmpty[y][x] = True
    
    for request in requests:
        target = request[0]
        if len(request) == 1:
            pick_boundary(0, 0, storage, target, isEmpty, height, width, set())
        else:
            for y in range(height):
                for x in range(width):
                    if storage[y][x] == target and not isEmpty[y+1][x+1]:
                        isEmpty[y+1][x+1] = True
    
    # print(*isEmpty, sep="\n")
    return sum(row[1:-1].count(False) for row in isEmpty[1:-1])