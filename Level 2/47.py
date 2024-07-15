"""

[3차] 파일명 정렬

그냥 파일명에서 첫번째로 등장하는 숫자집합을 찾아서 정렬하면 되는데

정규식을 쓰는거하고 안쓰는거 하고 한 번 차이가 얼마나 나나 둘다 작성해보겠음.

-> 그냥 쓰지 말자. for문으로 퉁치는게 나은듯




"""


def solution(Files):
    Nums = []
    Heads = []
    for File in Files:
        for i, c in enumerate(File):
            if c.isdigit():
                BeginI = i
                break

        EndI = len(File)
        for i in range(BeginI + 1, len(File)):
            if not File[i].isdigit():
                EndI = i
                break

        Heads.append(File[:BeginI].lower())
        Nums.append(int(File[BeginI:EndI]))

    Zipped = zip(Files, Heads, Nums)
    Sorted = sorted(Zipped, key=lambda x: (x[1], x[2]))
    Tr = list(zip(*Sorted))
    return Tr[0]


"""

이 버전이 좀 더 깔끔하긴 함.

"""


def solution2(Files):
    def SortKey(File):
        for i, c in enumerate(File):
            if c.isdigit():
                BeginI = i
                break

        EndI = len(File)
        for i in range(BeginI + 1, len(File)):
            if not File[i].isdigit():
                EndI = i
                break

        return (File[:BeginI].lower(), int(File[BeginI:EndI]))

    Files.sort(key=SortKey)
    return Files
