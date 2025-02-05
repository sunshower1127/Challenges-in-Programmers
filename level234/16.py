"""섬 연결하기

최소비용 연결이라...

어.. MST아닌가

원래 Prim이 그 unvisited하고 visited을 최소로 연결하는거고

Kruskal이 엣지를 비용순으로 오름차순으로 정렬해서 하나하나 연결하는거고

근데 이건 둘이 섞였다 그거네요

어지럽네.. 그냥 Kruskal이 맞는거 같긴한데

궁금한건 어떤 노드가 있으면 그 노드와 연결된 집합을 얻고 싶다 이거 아닙니까

물론 집합을 합치기도 해야하면 union-find 자료구조가 전통적으로 사용되는거고

그냥 찾기만 하는거면 list에다가 set을 집어넣고, 넣을때마다 node->set의index 를 저장하는 리스트를 수정해주면 되겠죠

union-find를 한 번 공부해보는것도 좋을듯

TODO: MST, Prim, Kruskal, union-find 정확히 정리해보기

트리를 가장 간단하게 만드는법 -> 배열에다가 부모 인덱스 저장하는거임.

Prim은 visited, unvisited를 연결하는 최소비용 엣지를 계속 찾아나가는거임. -> min_heap을 쓰면 된다.
Kruskal은 가장 짧은 엣지부터 살펴보는데, 둘 다 같은 집합에 속해있는지 확인하고, 아니면 합치는거임. -> union-find를 쓰면 된다.

union_find는 내가 구현한다고 하면
어.. set이 담긴 list를 만들고
그냥 합치면 되겠죠 뭐. set은 어차피 참조형이니깐 여러개가 리스트에 존재한다고 쳐도 동기화에 문제는 없을듯.

"""


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    visited = {0}
    cost_sum = 0

    while len(visited) < n:
        unvisited = {*range(n)} - visited
        for a, b, cost in costs:
            if a in visited and b in unvisited:
                cost_sum += cost
                visited.add(b)
                break
            if b in visited and a in unvisited:
                cost_sum += cost
                visited.add(a)
                break

    return cost_sum
