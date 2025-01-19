"""[1차] 캐시

대소문자 구분 x

LRU일때 (그냥 오래될수록 교체됨.)

캐시크기, hit는 1, miss는 5

"""

from collections import deque


def add_cache(cache, cache_set, cache_size, item):
    cache.append(item)
    cache_set.add(item)

    if len(cache) > cache_size:
        cache_set.remove(cache.popleft())


def hit_cache(cache, item):
    cache.remove(item)
    cache.append(item)


def solution(cache_size, cities):
    cache = deque()
    cache_set = set()
    time = 0

    for city in cities:
        city = city.lower()

        if city in cache_set:
            time += 1
            hit_cache(cache, city)
        else:
            time += 5
            add_cache(cache, cache_set, cache_size, city)

    return time
