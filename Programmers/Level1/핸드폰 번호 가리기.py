'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12948
'''
def solution(phone_number):
    return '*'*len(phone_number[:-4]) + phone_number[-4:]


print(solution("01033334444") == "*******4444")
print(solution(	"027778888") == "*****8888")