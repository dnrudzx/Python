import string
import itertools
import collections
import math
import re
#재귀 재한 늘리기
import sys
sys.setrecursionlimit(10**6)
#out of index 회피
#if a[-1:] == [i]:
##########################################################################################
''' a:숫자 / b:소문자 / c:대문자                                                          '''
''' str, list, tuple                                                                   '''
''' dict = key : index / value : abc                                                   '''
str_a, str_b, str_c = string.digits, string.ascii_lowercase, string.ascii_uppercase
list_a, list_b, list_c = list(str_a), list(str_b), list(str_c)
tuple_a, tuple_b, tuple_c = tuple(list_a), tuple(list_b), tuple(list_c)
dict_a, dict_b, dict_c = dict(enumerate(list_a)), dict(enumerate(list_b)), dict(enumerate(list_c))
##########################################################################################
''' 요소들을 한칸씩 띄어서 출력                                                             '''
#print(*str_a)
#print(*list_a)
#print(*tuple_a)
''' 딕셔너리는 key를 출력함                                                                '''
#print(*dict_a)
##########################################################################################
''' 숫자                                                                                 '''
''' 몫 / 나머지 출력                                                                      '''
#print(1234//3, 1234%3)
#print(*divmod(1234,3))                 #기본형태는 tuple
''' 진법변환 : 다른 진법을 10진법으로                                                        '''
# 10 진법 -> 2, 8, 16 진법                 -> 0b111100  0o74  0x3c
#print(format(60, '#b'), format(60, '#o'), format(60, '#x'))

# 10 진법 -> 2, 8, 16 진법(숫자부분만)       -> 111100 74 3c
#print(format(60, 'b'), format(60, 'o'), format(60, 'x'))

# 2, 8, 16 진법 -> 10진법       : 진수부호를 빼도 결과가 같다
#print(int('0b111100',2), int('0o74',8), int('0x3c', 16))
#print(int('111100',2), int('74',8), int('3c', 16))
''' 최대값(사전순 제일 끝) / 최소값(사전순 제일 앞) 출력 '''
#max(iterable)
#min(iterable)
''' 올림 / 내림 / 반올림 / 제곱근 '''
#math.ceil(number)
#math.floor(number)
#round(number)
#math.sqrt(number)
##########################################################################################
''' 문자열                                                                               '''
''' 좌 / 우 / 가운데 정렬                                                                  '''
#print('왼쪽정렬'.ljust(30,' '))             #문자열.ljust(출력글자수, 공백문자)
#print('우측정렬'.rjust(30))                 #공백문자를 안쓰면 ' '와 같이 출력됨
#print('가운데정렬'.center(30,'#'))           #공백문자를 다른글자로 바꿀 수 있음
''' 대소문자 전환 '''
#print('aAbBcCdD'.swapcase())
''' 대소문자 확인'''
#print(str_b.islower())
#print(str_b.isupper())
''' 알파벳만 있는지 / 숫자만 있는지 '''
#print(str_a.isalpha())
#print(str_a.isdigit())
''' 이어붙이기                                                                            '''
#print('#'.join(list_a))                     #list / tuple의 요소를 이어붙임
##########################################################################################
''' map 함수                                                                            '''
#print(list(map(int, list_a)))               #정수로 바꾸기
#print(list(map(len, list_a)))               #길이로 바꾸기
#print(list(map(int, input().split())))      #입력문자열을 끊고(split) 정수로 변환(int)
#print(list(map(list, zip(list_a, sorted(list_b), reversed(list_c)))))
                                             #인덱스별로 리스트 묶기 / sorted나 reversed 사용 가능
#print(list(map(list,zip(*[[1,2,3], [4,5,6], [7,8,9]]))))
                                             # -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
                                             # 2차원 리스트 뒤집기
##########################################################################################
'''sorted'''    #sorted(리스트이름, key=정렬방식, reverse=거꾸로 정렬여부)
#print(sorted(list_a, reverse=True))        #거꾸로 정렬
'''     길이순 정렬 : 리스트의 요소에 대한 설명이 필요하면 lambda 사용
list_len = ['1111','111','11','1']
print(sorted(list_len, key=lambda x : len(x)))
'''
##########################################################################################
'''enumerate()'''   #반복문에서 인덱스랑 요소를 같이 줌
'''
for index, item in enumerate(list_a):
    print(index, item)
'''
##########################################################################################
'''zip()'''
'''반복문에서 리스트 두개의 아이템 동시에 꺼내기
for a_item, b_item in zip(list_a, list_b):
    print(a_item, b_item)
'''
'''2차원 리스트 90도 회전
배열_2차원 = [[1,2,3],[4,5,6],[7,8,9]]
print(배열_2차원)
print(list(zip(*배열_2차원[::-1])))
'''
##########################################################################################
'''itertools 라이브러리'''
''' 하나의 리스트 
print(list(itertools.permutations(list_a, 2)))                      순열 / 중복 x
print(list(itertools.product(list_a, repeat=2)))                    순열 / 중복 O
print(list(itertools.combinations(list_a, 2)))                      조합 / 중복 x
print(list(itertools.combinations_with_replacement(list_a, 2)))     조합 / 중복 O
'''
a = list(itertools.combinations(list_a, 2))
del a[0]
print(a)
'''     모든 조합 구하기(곱집합)
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
'''
'''     순열 : permutations : 서로 다른 모든 경우 : permutations(iterable, 합쳐지는 수)
print(list(map(''.join, itertools.permutations(list_a, 2))))
'''
'''     조합 : combinations : 서로 다른 순서가없는 모든 경우 : combinations(iterable, 합쳐지는 수)
print(list(map(''.join, itertools.combinations(list_a, 2))))
'''
##########################################################################################
'''functools 라이브러리'''
#여러가지 있는데 아직 공부 안함
##########################################################################################
'''collections 라이브러리'''
'''     Counter()함수 
collections.Counter(iterable)   #딕셔너리 형태로 리턴됨
'''
'''     deque 자료형
deque_a = collections.deque(list_a)
deque_a.append('10')        #오른쪽에 추가
deque_a.pop()               #오른쪽 삭제
deque_a.appendleft('-1')    #왼쪽에 추가
deque_a.popleft()           #왼쪽 삭제
deque_a.extend(list_b)      #오른쪽에 합치기
deque_a.extendleft(list_b)  #왼쪽에 합치기
'''
##########################################################################################
'''re 라이브러리'''
