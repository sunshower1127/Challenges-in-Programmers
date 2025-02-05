"""기능개발

progresses 에 순서대로 현재 작업 진행률이 적혀있음.
[93, 30, 55] -> 반드시 첫번째가 끝나야 두번째도 끝낼 수 있음.

동시에 진행되는 속도는 speeds에 있음
[1, 30, 5] -> 하루에 이만큼씩 진행됨.

그래서 진행이 완료될때마다 몇개의 작업이 완료되는지를 반환

[2, 1] -> 1,2번 작업이 동시에 완료되고, 3번째 작업은 마지막에 완료.

어떠한 시간복잡도 압박이 없기때문에 그냥 풀면됨.
물론 시간복잡도 압박이 있다면(사실 있는지 없는지 모르겠음) for을 작업 기준으로 돌려야함.
아닌가 그냥 똑같나 모르겠다

"""


def solution(progresses, speeds):
    N = len(progresses)
    Idx = 0
    List = []
    while True:
        for i in range(Idx, N):
            progresses[i] += speeds[i]

        NewIdx = Idx
        while True:
            if NewIdx == N:
                break
            if progresses[NewIdx] >= 100:
                NewIdx += 1
            else:
                break

        if NewIdx != Idx:
            List.append(NewIdx - Idx)
            Idx = NewIdx

            if Idx == N:
                break

    return List
