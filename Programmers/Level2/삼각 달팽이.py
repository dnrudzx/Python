'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
'''


def solution(n):
    answer = [0 for num in range(n + 1) for _ in range(num)]
    mode = 1  # 방향을 결정(왼쪽 아래로 / 오른쪽으로 / 왼쪽 위로)
    num = 1  # 각 인덱스에 들어갈 숫자
    idx = 0  # answer의 인덱스
    level = 0  # 층을 표시(mode1/3의 경우 level에 따라 다른 인덱스 변화가 필요함)

    while True:
        if answer.count(0) == 0: break
        if mode == 1:
            for _ in range(n):
                idx += level
                answer[idx] = num
                num += 1
                level += 1
            mode = 2
            n -= 1
        elif mode == 2:
            for _ in range(n):
                idx += 1
                answer[idx] = num
                num += 1
            mode = 3
            n -= 1
        elif mode == 3:
            for _ in range(n):
                idx -= level
                answer[idx] = num
                num += 1
                level -= 1
            mode = 1
            n -= 1

    return answer


print(solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(solution(6) == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])