'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42576
'''
def solution(participant, completion):
    import collections
    participant_dict = dict(collections.Counter(participant))
    completion_dict = dict(collections.Counter(completion))
    for key in participant_dict.keys():
        if key not in completion_dict:
            return key
        elif participant_dict[key] - completion_dict[key] == 1:
            return key


print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']) == 'leo')
print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == 'vinko')
print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == 'mislav')