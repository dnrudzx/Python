'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/49993
'''
def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        skill_index = 0
        before = True
        success = True
        for i in skill:
            if i not in skill_tree:
                if before:
                    before = False
                    continue
            else:
                if before == False:
                    success = False
                    break
                if skill_index > skill_tree.index(i):
                    success = False
                    break
                else:
                    skill_index = skill_tree.index(i)
        if success:
            count += 1
    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2)