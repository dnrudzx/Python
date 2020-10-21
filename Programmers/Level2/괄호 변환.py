'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60058
'''
def p2(u,v):
    u = u + v[:2]
    v = v[2:]
    if u.count('(') != u.count(')'):
        u, v = p2(u,v)
    return u,v

def p3_0(u):
    for i in range(len(u)):
        if u[:i].count('(') < u[:i].count(')'):
            return False
    return True

def p4(u,v):
    result = '(' + solution(v) + ')'
    for i in range(1,len(u)-1):
        if u[i] == '(': result += ')'
        else: result += '('
    return result

def solution(p):
    if p == '':
        return p
    u = ''
    v = p
    u, v = p2(u, v)
    if p3_0(u) == True:
        return u + solution(v)
    else:
        u = p4(u,v)
    return u


print(solution("(()())()") == "(()())()")
print(solution(")(") == "()")
print(solution("()))((()") == "()(())()")