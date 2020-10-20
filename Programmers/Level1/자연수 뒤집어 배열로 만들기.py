'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12932
'''
def solution(n):
    return list(reversed([int(i) for i in str(n)]))


print(solution(12345) == [5,4,3,2,1])