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
