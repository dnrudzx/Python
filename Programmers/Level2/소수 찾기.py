'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42839
'''
def check(non_check):
    non_check_list = set()
    for i in non_check:
        non_check_list.add(int(''.join(i)))
    non_check_list -= {0,1}
    if len(non_check_list) > 0:
        for i in range(2,max(non_check_list)+1):
            non_check_list -= set(range(2*i, max(non_check_list)+1,i))
            if len(non_check_list) == 0:
                return {}
    return non_check_list

def solution(numbers):
    import itertools
    answer = set()
    #print(list(itertools.permutations(numbers,2)))
    for i in range(1,len(numbers)+1):
        non_check = list(itertools.permutations(numbers,i))
        check_list = check(non_check)
        if len(check_list) > 0:
            answer.update(check_list)
    print(answer)
    return len(answer)

print(solution('17') == 3)
print(solution('011') == 2)