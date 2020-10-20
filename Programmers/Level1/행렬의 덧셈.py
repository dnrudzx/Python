'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12950
'''
def solution(arr1, arr2):
    result = []
    for lst1, lst2 in zip(arr1, arr2):
        add_lst = []
        for a,b in zip(lst1, lst2):
            add_lst.append(a+b)
        result.append(add_lst)
    return result


print(solution(	[[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]])
print(solution([[1], [2]], [[3], [4]]) == 	[[4], [6]])