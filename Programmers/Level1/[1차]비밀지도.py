'''
문제 출처 :https://programmers.co.kr/learn/courses/30/lessons/17681
'''
def solution(n, arr1, arr2):
    temp = [str(format(i, 'b')).rjust(n,'0') for i in arr1]
    arr1 = temp
    temp = [str(format(i, 'b')).rjust(n,'0') for i in arr2]
    arr2 = temp
    result = []
    for a,b in zip(arr1,arr2):
        out = ''
        for c,d in zip(a,b):
            if c == '0' and d == '0':out += ' '
            else: out += '#'
        result.append(out)
    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == ["#####", "# # #", "### #", "#  ##", "#####"])
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) == ["######", "###  #", "##  ##", " #### ", " #####", "### # "])