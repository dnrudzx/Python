'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12912
'''
def solution(a, b):
    answer = 0
    if a > b: nums = [n for n in range(b,a+1)]
    elif a==b: return a
    else: nums = [n for n in range(a,b+1)]
    for i in nums:
        answer += i
    return answer


print(solution(3, 5) == 12)
print(solution(3, 3) == 3)
print(solution(5, 3) == 12)