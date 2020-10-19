'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42840
'''
def solution(answers):
    result = []
    collect_list = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for index, answer in enumerate(answers):
        a_index = index % len(a)
        b_index = index % len(b)
        c_index = index % len(c)
        if answer == a[a_index]: collect_list[0] += 1
        if answer == b[b_index]: collect_list[1] += 1
        if answer == c[c_index]: collect_list[2] += 1
    for index, i in enumerate(collect_list):
        if i == max(collect_list):
            result.append(index + 1)
    return result


print(solution(	[1, 2, 3, 4, 5]) == [1])
print(solution(	[1, 3, 2, 4, 2]) == [1,2,3])