'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12903
'''
def solution(s):
    if len(s) % 2 ==1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]


print(solution("abcde") == 'c')
print(solution("qwer") == 'we')