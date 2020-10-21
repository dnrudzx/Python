'''
문제 출처 :https://programmers.co.kr/learn/courses/30/lessons/62048
'''
def solution(w,h):
    #a = 최대 공약수를 구하고
    #w//a + h//a -1 = b : 정확히 잘리는 작은 사각형
    #w//w//a = c : 작은 사각형의 수 = a
    #result = w*h - b*c
    a = 1
    for i in range(1, min(w,h)+1):
        if w%i == 0 and h%i == 0: a = i
    b = w/a + h/a -1
    return w*h - b*a


print(solution(8,12) == 80)