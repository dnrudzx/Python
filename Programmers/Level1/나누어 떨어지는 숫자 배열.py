'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12910
'''
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0: answer.append(i)
    if len(answer) == 0: return [-1]
    return sorted(answer)


print(solution(	[5, 9, 7, 10], 5) == [5,10])
print(solution(	[2, 36, 1, 3], 1) == [1,2,3,36])
print(solution(	[3, 2, 6], 10) == [-1])