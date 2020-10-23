'''
collections : 특수한 자료형들 제공
'''
from collections import *

###########################################################
'''ChainMap : 여러 매핑을 연결해 단일 단위로 취급
        새로운 딕셔너리를 만들어 update를 호출하는 경우 효율성을 높임'''
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
a = dict(ChainMap(adjustments, baseline))

###########################################################
'''Counter : 목록에 있는 단어의 빈도를 집계
        커다란 String문자열에서 가장 많은 빈도 찾기에 유용할듯'''
color = ['red', 'blue', 'red', 'green', 'blue', 'blue']
#기본 출력
#print(Counter(color))
#객체 생성_1
c = Counter(blue=3, red=2, green=1)
#객체 생성_2
c = Counter(color)
'''update'''
c.update({'blue':-1, 'red':3, 'black':4})
'''element'''
#print(list(c.elements()))               #빈도수 순서
#print(sorted(c.elements()))             #사전 순서
'''most_common(n) : 빈도수 순으로 상위 n개를 반환'''
#print(c.most_common(2))
'''subtract(iterable) : 요소 빼기
    리턴값이 없고, 포인터로 바로 쳐내는 거니까 조심해서 사용'''
#c.subtract(color)
#산술연산(+,-,*,/) 가능
#집합연산(&,|) 가능

###########################################################
'''deque : 양방향 데이터 처리용 queue형 자료형
    리스트랑 사용법이 많이 비슷함'''
#append(x)              : 오른쪽에 요소 하나 추가
#appendleft(x)          : 왼쪽에 요소 하나 추가
#extend(iterable)       : 오른쪽에 iterable객체 추가
#extendleft(iterable)   : 왼쪽에 iterable객체 추가
#pop()                  : 오른쪽 끝 요소 빼서 반환
#popleft()              : 왼쪽 끝 요소 빼서 반환
#rotate(n)              : 요소들을 n만큼 회전 시켜줌(음수 : 왼쪽 / 양수 : 오른쪽)

###########################################################
'''defaultdict : dict와 같은 구조를 가지고 key가 없는 경우 default값 적용'''
#기본 구조
def default_factory(): return 'null'        #null대신 다른거 넣어도 됨
dd = defaultdict(default_factory, a=3,b=2)
dd = defaultdict(list,a=3,b=2)
dd = defaultdict(set,a=3,b=2)
dd = defaultdict(int,a=3,b=2)
#print(dd)

###########################################################
'''OrderedDict : 입력된 아이템들의 순서를 기억하는 dict'''
#기본 딕셔너리
#d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange':2}
#키를 기준으로 생성
#ordered_1 = OrderedDict(sorted(d.items(), key=lambda x:x[0]))
#값을 기준으로 생성
#ordered_2 = OrderedDict(sorted(d.items(), key=lambda x:x[1]))
'''popitem(last=True)'''
#print(ordered_1)
#print(ordered_1.popitem(True))      #마지막 아이템을 뺌
#print(ordered_1.popitem(False))     #첫번째 아이템을 뺌
'''move_to_end(key, last=True)'''
#print(ordered_2)
#ordered_2.move_to_end('orange',True)
#print(ordered_2)
#ordered_2.move_to_end('orange',False)
#print(ordered_2)

###########################################################
'''nametuple : key값으로 접근 가능한 투플(딕셔너리 + 튜플)
    메소드가 없는 클래스를 만드록 객체를 선언하는 느낌'''
#일반 투플
a = ('John', 28, '남')
#print('%s는%d세의 %s성입니다'%a)
#nametuple 생성
Person = namedtuple('Person', 'name, age, gender')
#객체 생성
P_a = Person(name='Jonh', age=28, gender='남')
P_b = Person._make(['Tom', 24,'남'])
#print(P_a)
#print(P_a.name, P_a.age, P_a.gender)
#객체 수정
P_a = P_a._replace(name='Neo')
#print(P_a)






