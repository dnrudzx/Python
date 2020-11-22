'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42883
'''
def solution(number, k):
    answer = ''

    number = list(number)
    k = len(number) - k
    idx = -1
    for i in range(1,k+1):
        val = 0
        for j in range(idx+1,len(number)-k+i):
            if val < int(number[j]):
                val = int(number[j])
                if val == 9:
                    idx = j
                    break
                idx = j
        answer += str(val)

    return answer

print(solution('1924',2))
print(solution('1231234',3))
print(solution('4177252841',4))