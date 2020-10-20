'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12969
'''
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print(''.join(['*' for i in range(a)]))

#옛날 문제라 solution으로 안들어가고 input으로 들어감