'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12940
'''
def p1(num):
    num_set = set()
    for i in range(1,num+1):
        if i in num_set:
            break
        if num%i==0:
            num_set.add(i)
            num_set.add(num//i)
    return num_set
def solution(n, m):
    answer = []
    n_set = p1(n)
    m_set = p1(m)
    answer.append(max(n_set&m_set))
    answer.append(n*m/answer[0])
    return answer


print(solution(3,12) == [3,12])
print(solution(2,5) == [1,10])