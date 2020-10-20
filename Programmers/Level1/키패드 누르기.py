'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/67256
'''
def distance(number, hand):
    num_list = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    result = [0,0]
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            if num_list[i][j] == number:
                result[0] += i
                result[1] += j
            if num_list[i][j] == hand:
                result[0] -= i
                result[1] -= j
    return abs(result[0])+abs(result[1])
def solution(numbers, hand):
    result = ''
    left = '*'
    right = '#'
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            result += 'L'
            left = number
        elif number == 3 or number == 6 or number == 9:
            result += 'R'
            right = number
        else:
            if distance(number,left) > distance(number,right):
                result += 'R'
                right = number
            elif distance(number, left) < distance(number, right):
                result += 'L'
                left = number
            else:
                if hand == 'left':
                    result += 'L'
                    left = number
                else:
                    result += 'R'
                    right = number
    return result


print(solution(	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == 	"LRLLLRLLRRL")
print(solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == 	"LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == 	"LLRLLRLLRL")