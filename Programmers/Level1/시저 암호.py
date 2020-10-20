'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12926
'''
def solution(s, n):
    import string
    answer = ''
    lower, upper = list(string.ascii_lowercase), list(string.ascii_uppercase)
    for i in s:
        if i == ' ': answer += ' '
        elif i.islower(): answer += lower[(lower.index(i)+n)%len(lower)]
        else: answer += upper[(upper.index(i)+n)%len(upper)]
    return answer


print(solution(	"AB", 1) == 'BC')
print(solution(	"z", 1) == 'a')
print(solution(	"a B z", 4) == 'e F d')