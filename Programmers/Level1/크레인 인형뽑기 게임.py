'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/64061
'''
def solution(board, moves):
    answer = 0
    a = []
    for i in list(zip(*board[::-1])):   #이중리스트 돌리기
        a.append(list(i))
    result = []
    for move in moves:
        while True:
            try:
                doll = a[move - 1].pop()
            except:
                break
            if doll != 0:
                result.append(doll)
                break
        if len(result) > 1:
            if result[-1] == result[-2]:
                result = result[:-2]
                answer += 2
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]) == 4)
