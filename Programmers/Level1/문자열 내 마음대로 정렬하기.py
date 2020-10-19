'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12915
'''
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


print(solution(	["sun", "bed", "car"], 1) == ["car", "bed", "sun"])
print(solution(	["abce", "abcd", "cdx"], 2) == 	["abcd", "abce", "cdx"])