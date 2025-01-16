"""우박수열 정적분

이게 그러니깐
값을 알아내서 구간값을 구한다음에 어떻게 더할까 그거 아님?
흠
그냥 다 더한 다음에


내가 가진 잡기술들 최대한 활용해봄.
일단 설명 읽고 이해 안가더라도 예제로 가서 맞춰보기.

내가 제대로 이해했는지 확인하는게 제일 중요함.
그래서 calculate 함수 구현을 제일 뒤로 뺐음.
그냥 리터럴 리턴하게 했고 -> 어차피 이래도 테스트엔 문제 없으니깐
빠르게 아래부터 완성하고, 예외 처리하고 위로 올라옴.


tip1: yield 사용한건 return 값이 Generator임. Iteator랑 비슷함. 그래서 list로 감싸주던가 해야됨

"""


def calculate(k):
    yield k

    while k > 1:
        if k % 2 == 0:
            k //= 2
            yield k
        else:
            k *= 3
            k += 1
            yield k


def solution(k, ranges):
    values = list(calculate(k))
    length = len(values)
    result = []

    for begin, end in ranges:
        if end <= 0:
            end = length + end - 1
            if not (begin <= end < length):
                result.append(-1)
                continue

            v = 2 * sum(values[begin : end + 1]) - values[begin] - values[end]
            v /= 2
            result.append(v)

    return result
