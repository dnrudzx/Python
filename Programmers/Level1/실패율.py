'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42889
'''
def solution(N, stages):
    stage_dict = {}
    loser = 0
    for i in range(1,N+1):
        now_stage = stages.count(i)
        if now_stage == 0:
            stage_dict[i] = 0
        else:
            stage_dict[i] = now_stage/(len(stages) - loser)
        loser += now_stage
    stage_dict = sorted(stage_dict.items(), key=lambda x:x[1], reverse = True)
    return [i for i,j in stage_dict]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5])
print(solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3])