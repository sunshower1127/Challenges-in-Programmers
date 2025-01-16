"""

오픈 채팅방

그냥 구현인데
record가 좀 길거든요 n까지 허용
효율성을 위해서 uid로 들어왔습니다, 나갔습니다를 줄지어놓고,
Enter했을때 기존에 없는 uid면 -> 새로 추가
Change면 값 바꾸기.
해서 마지막에 한번에 포맷팅하면ㄷ ㅚㄹ듯.
dict에서 uid -> 닉네임
연결시키면 되고,

아 예외가 있네 -> 나가서 닉네임 바꾸는건 Change가 아님
예외처리해주고

이게 일단 가장 쉬운 방법으로 짜보고 -> 안되면 업그레이드 하는 식으로 할까

일단 모듈화를 시키고.

변수명을 간단하게 만드는 방법은 -> 그냥 함수안에 집어넣는거임.

코드를 다 짜고 하나씩 검사하는건 뭐랄까 도중에 잘못되면 다 갈아엎어야하는 상황에 처함.

자잘한 목표를 계속 잡아 나가는게 중요함.

Leave할때 전 닉네임을 찾아야함.

근데 어차피 바꿀거면? -> 마지막에 한번에 닉네임 바꾸는게 효율적임

uid 검색해서 마지막 Change or 마지막 Enter에서 나온 닉네임 찾기.

마지막 닉네임 찾기
    input -> record
    output -> {uid : 최종닉네임}
"""


def FindNick(Record):
    Dict = {}

    for Line in reversed(Record):
        Data = Line.split(" ")
        if Data[0] == "Leave":
            continue
        Uid, Nick = Data[1], Data[2]

        if Uid in Dict:
            continue
        Dict[Uid] = Nick
    return Dict


def solution(Record):
    NickDict = FindNick(Record)
    Result = []

    for Line in Record:
        Data = Line.split(" ")
        if Data[0] == "Change":
            continue
        Uid = Data[1]
        Nick = NickDict[Uid]
        Result.append(
            f'{Nick}님이 {"들어왔습니다." if Data[0]=="Enter" else "나갔습니다."}'
        )

    return Result
