'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12899
'''
def solution(n):
    #하나 뺴서 3진법
    result = ''
    while True:
        n = n-1
        if n%3 == 0 : result = '1' + result
        elif n%3 == 1: result = '2' + result
        else: result = '4' + result
        if n <3: break
        else: n = n//3
    return result


print(solution(1) == '1')
print(solution(2) == '2')
print(solution(3) == '4')
print(solution(4) == '11')