'''https://kimdoky.github.io/python/2019/11/24/python-itertools/
itertools : 효율적인 반복을 위한 라이브러리
'''
import itertools

##############무한 반복자##############
#count(start) : start부터 1씩 상승
#count(start, step) : start부터 step씩 상승
#cycle(iterable) : iterable자료형의 요소들 반복
#repeat(element) : 요소 하나 무한반복
#repeat(element, n) : 요소하나 n번 반복


##############반복자##############
#itertools.accumulate(iterable) : 0, 0+1, 0+1+2 ...
#itertools.chain(iterable_1, iterable_2) : 그냥 이어버림
#itertools.chain.from_iterable() : 위랑 비슷한데 더 세세하게 쪼개짐
#itertools.compress(iterable, [boolean]) : iterable한 데이터와 매칭해서 True(1)이면 표시


##############조합 반복자##############
#itertools.product()                         #결과중복(순서바꿀때) O | 요소중복 O
#itertools.permutations()                    #결과중복(순서바꿀때) O | 요소중복 X
#itertools.combinations_with_replacement()   #결과중복(순서바꿀때) X | 요소중복 O
#itertools.combinations()                    #결과중복(순서바꿀때) X | 요소중복 X
