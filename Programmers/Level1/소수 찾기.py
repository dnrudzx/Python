'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12921
'''
def solution(n):
    num_set = set(range(2,n+1))
    for i in range(2,n+1):
        if i in num_set:
            num_set -= set(range(2*i,n+1,i))
    return len(num_set)


print(solution(10) == 4)
print(solution(5) == 3)