'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
'''
def solution(numbers):
    answer = set()  #중복제거
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])