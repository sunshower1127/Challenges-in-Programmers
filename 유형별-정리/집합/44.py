"""스킬트리

스킬 순서가 나오고

가능한지 판별하기

이것도 서브셋인데
얘는 순서를 따지고
중간에 다른거 들어가는건 된다는 거네

근데 반드시 다 안들어가도 됨.

in 최적화는 역시 set임.

"""


def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        i = 0
        for cur_skill in skill_tree:
            if cur_skill != skill[i]:
                continue

            i += 1
            if i == len(skill):
                break

        skill_set = set(skill_tree)
        if i == len(skill) or all(s not in skill_set for s in skill[i:]):
            result += 1

    return result
