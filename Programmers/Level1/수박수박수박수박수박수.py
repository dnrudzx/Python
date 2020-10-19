'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12922
'''
def solution(n):
    answer = '수박' * ((n+1)//2)
    return answer[:n]


print(solution(3) == '수박수')
print(solution(4) == '수박수박')