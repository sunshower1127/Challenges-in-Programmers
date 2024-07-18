"""

스킬트리

skill에는 스킬트리 순서가 적혀있음 -> CBD면 반드시 C -> B -> D 순서대로 배워야함

선행스킬 순서 skill_trees가 주어질 때 가능한 스킬트리 개수를 return

시간복잡도는 딱히 안따져도 되는듯.

26*20*26 이라서 뭐 해봤자 8000정도라서...

근데 최적화는 그냥 set쓰면 됨. 아니면 dict로 반대방향 만들던가.



"""


def solution(skill, skill_trees):
    Cnt = 0
    Skills = set(skill)

    for SkillTree in skill_trees:
        Str = ""
        for c in SkillTree:
            if c in Skills:
                Str += c

        if skill.find(Str) == 0:
            Cnt += 1

    return Cnt


# def solution(skill, skill_trees):
#     Cnt = 0
#     Dict = {Skill: i for i, Skill in enumerate(skill)}

#     for SkillTree in skill_trees:
#         Idx = 0
#         for c in SkillTree:
#             if Dict.get(c) is not None:
#                 if Dict[c] == Idx:
#                     Idx += 1
#                 else:
#                     break
#         else:
#             Cnt += 1

#     return Cnt
