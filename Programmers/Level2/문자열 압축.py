'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60057
'''
import math


def solution(s):
    best = len(s)
    zip_count = 1

    while True:
        minus = 0
        count = 0

        before = False
        upper = 0
        upper_case = 0
        temp = s
        while len(temp) > zip_count:
            a = temp[0:zip_count]
            b = temp[zip_count:2 * zip_count]
            temp = temp[zip_count:]
            if a == b:
                minus += zip_count
                if before == False:
                    count += 1
                else:
                    upper += 1
                    if upper == 8:
                        upper_case += 1
                    if upper == 98:
                        upper_case += 1
                    if upper == 998:
                        upper_case += 1

                before = True
            else:
                before = False
                upper = 0
        result_len = len(s) - minus + count + upper_case

        if best > result_len:
            best = result_len
        if zip_count > math.ceil(len(s) / 2):
            break
        zip_count += 1

    return best


print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution(	"xababcdcdababcdcd") == 17)
print(solution("aaa") == 2)