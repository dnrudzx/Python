'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42883
'''
def solution(number, k):
    answer = ''

    number = list(number)
    k = len(number) - k
    while k > 0:
        if k>1:
            lst = number[:-(k-1)]
        else:
            lst = number
        num = max(lst)
        answer += str(num)
        idx = number.index(num)
        number = number[idx+1:]
        k -= 1

    return answer

print(solution('1924',2))
print(solution('1231234',3))
print(solution('4177252841',4))