'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42586
'''
from collections import deque

def solution(progresses, speeds):
    result = []
    speeds = deque(speeds)

    while len(progresses) != 0:
        temp = deque()
        count = 0
        for a, b in zip(progresses, speeds):
            temp.append(a + b)
            progresses = temp

        while True:
            if len(progresses) == 0: break
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else: break
        if count != 0: result.append(count)

    return result


print(solution([93, 30, 55], [1, 30, 5]) == [2,1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1,3,2])