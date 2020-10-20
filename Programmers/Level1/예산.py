'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12982
'''
def solution(d, budget):
    answer = 0
    d = sorted(d, reverse=True)
    while True:
        if len(d) == 0: break
        budget -= d.pop()
        if budget < 0:
            return answer
        answer += 1
    return answer


print(solution(	[1, 3, 2, 5, 4], 9) == 3)
print(solution(	[2, 2, 3, 3], 10) == 4)