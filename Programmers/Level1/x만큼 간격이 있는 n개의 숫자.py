'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12954
'''
def solution(x, n):
    return [i*x for i in range(1,n+1)]


print(solution(2,5) == [2, 4, 6, 8, 10])
print(solution(4,3) == [4, 8, 12])
print(solution(-4,2) == [-4, -8])