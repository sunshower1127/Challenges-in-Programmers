def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    return dist


"""플로이드 워셜

중요한건 k가 제일 바깥쪽에 있다는거.

"""
