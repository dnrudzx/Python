'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12937
'''
def solution(num):
    if num % 2 == 0: return 'Even'
    return 'Odd'


print(solution(3) == 'Odd')
print(solution(4) == 'Even')