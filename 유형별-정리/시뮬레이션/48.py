"""오픈채팅방

닉네임은 안에서, 밖에서 모두 변할 수 있음.
어디서 닉네임을 변환시키던 반드시 채팅창 로그에 있는 닉네임이 변해야함.

닉네임 중복가능. uid로 판단함.

밖에서 닉네임 변경하면 닉네임 변경 로그가 안뜸.

유저는 최대 100000
로그도 최대 100000

매번 바꾸는건 부담되니깐
마지막에 한번에 로그 출력하는걸로 하자.

근데 이건 문자열이 아니라 그냥 defaultdict인데?

"""

from collections import defaultdict


def solution(records):
    outputs = []
    uid2name = defaultdict(str)

    for record in records:
        data = record.split(" ")
        action, uid = data[0:2]

        if action == "Leave":
            outputs.append((uid, "님이 나갔습니다."))
            continue

        name = data[2]

        if action == "Enter":
            if uid2name[uid] != name:
                uid2name[uid] = name
            outputs.append((uid, "님이 들어왔습니다."))
        else:  # Change
            uid2name[uid] = name

    return [uid2name[uid] + content for uid, content in outputs]
