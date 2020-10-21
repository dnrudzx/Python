'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42587
'''
def solution(priorities, location):
    count = 0
    while True:
        if priorities[0] == max(priorities):
            count += 1
            if location == 0:
                return count
            priorities = priorities[1:]
        else:
            temp = priorities[0]
            priorities = priorities[1:]
            priorities.append(temp)
        location -= 1
        if location == -1:
            location += len(priorities)


print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)