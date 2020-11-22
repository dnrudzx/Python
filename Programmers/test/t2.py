def check(a):
    if a == '':return True
    stack = 0
    for i in a:
        if i == '(': stack += 1
        else:
            stack -= 1
            if stack < 0: return False
    return True
def solution(arr1, arr2):
    for i in range(len(arr1)-1,-1,-1):
        if arr1[i][0] == ')':
            del arr1[i]
    for i in range(len(arr2)-1,-1,-1):
        if arr2[i][-1] == '(':
            del arr1[i]
    answer = 0
    a1 = []
    a2 = []
    for i in arr1:
        a1.append(i.count('(')-i.count(')'))
    for i in arr2:
        a2.append(i.count('(')-i.count(')'))
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i] + a2[j] == 0:
                if check(arr1[i]+arr2[j]):
                    answer += 1
    return answer