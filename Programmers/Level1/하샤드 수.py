'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12947
'''
def solution(x):
    if x % sum([int(i) for i in str(x)]) == 0: return True
    return False


print(solution(10) == True)
print(solution(12) == True)
print(solution(11) == False)
print(solution(13) == False)