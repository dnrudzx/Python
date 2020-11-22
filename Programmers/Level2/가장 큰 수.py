'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42746
'''
def solution(numbers):
    nums = [(i,str(numbers[i])*3) for i in range(len(numbers))]
    nums = sorted(nums, key=lambda x:x[1], reverse=True)
    result = ''
    for i in nums:
        result += str(numbers[i[0]])

    if result[0] == '0': return '0'
    return result

print(solution([6,10,2]))
print(solution([3,30,34,5,9,1000]))
print(solution([40,403]))
print(solution([0,0,0]))