'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42584
'''
def solution(prices):
    answer = []
    for i in range(len(prices)):
        stack = 0
        for j in range(i+1, len(prices)):
            stack += 1
            if prices[i] > prices[j]: break
        answer.append(stack)
    return answer


print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])