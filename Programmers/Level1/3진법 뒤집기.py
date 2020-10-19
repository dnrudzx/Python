'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68935
'''
def solution(n):
    answer = ''
    while n >= 3:
        answer += str(n%3)
        n = n//3
    answer += str(n)
    result = 0
    for i in range(len(answer)):
        result += int(answer[-i-1])*(3**i)
    return result


print(solution(45) == 7)
print(solution(125) == 229)