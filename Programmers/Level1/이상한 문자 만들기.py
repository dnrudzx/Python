'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12930
'''
def solution(s):
    arr = s.split(' ')
    for lst_idx, word in enumerate(arr):
        temp = ''
        for word_idx, char in enumerate(word):
            if char.isalpha():
                if word_idx % 2 == 0: temp += char.upper()
                else: temp += char.lower()
            else: temp += char
        arr[lst_idx] = temp
    return ' '.join(arr)


print(solution(	"try hello world") == "TrY HeLlO WoRlD")