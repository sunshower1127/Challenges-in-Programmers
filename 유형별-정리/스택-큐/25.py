"""

[1차] 캐시

LRU -> 가장 오랫동안 참조되지 않은 페이지를 교체
cache hit -> 1초
cache miss -> 5초
했을때 총 시간은?

deque(maxlen=cacheSize)를 쓸 수도 있다.
이걸 외워야하는지는.. 흠..
어쨋든 maxlen을 초과해 append를 하면 반대쪽이 삭제된다.
"""

from collections import deque


def solution(cacheSize, cities):
    Cache = deque()

    Time = 0

    if cacheSize == 0:
        return len(cities) * 5

    for City in cities:
        City = City.lower()
        if City in Cache:
            Cache.remove(City)
            Cache.append(City)
            Time += 1
        else:
            if len(Cache) == cacheSize:
                Cache.popleft()
            Cache.append(City)
            Time += 5

    return Time
