'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12943
'''
def p1(num): return num/2
def p2(num): return 3*num + 1
def solution(num):
    answer = 0
    while num != 1:
        if answer == 500: return -1
        if num % 2 == 0: num = p1(num)
        else: num = p2(num)
        answer += 1
    return answer


print(solution(6) == 8)
print(solution(16) == 4)
print(solution(626331) == -1)