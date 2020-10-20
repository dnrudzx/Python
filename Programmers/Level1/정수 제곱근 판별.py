'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12934
'''
def solution(n):
    if (n**0.5).is_integer(): return ((n**0.5)+1)**2
    return -1
    ''' 제곱근으로 sqrt를 쓰는게 일반적이지만 0.5를 제곱해도 값이 같다
    from math import sqrt
    if sqrt(n).is_integer(): return (sqrt(n)+1)**2
    return -1
    '''


print(solution(121) == 144)
print(solution(3) == -1)