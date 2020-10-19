'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12916
'''
def solution(s):
    if s.lower().count('p') == s.lower().count('y'): return True
    return False


print(solution(	"pPoooyY") == True)
print(solution("Pyy") == False)