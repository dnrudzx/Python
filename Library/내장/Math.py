'''
Math : 숫자 관련 라이브러리
'''
from math import *
'''소수점 처리'''
#print(ceil(1.1111))         #올림
#print(floor(1.1111))        #내림
#print(trunc(-1.1111))       #소수점버림
#print(modf(3.14))           #소수부와 정수부를 나눠서 출력(소수부의 경우 2진체계 오류가 있음)
'''함수'''
#print(pow(3,2))             #a의 b제곱
#print(sqrt(4))              #x의 제곱근
#print(factorial(4))         #펙토리얼 반환
#print(gcd(6,8))             #최대 공약수
#print(6*8/gcd(6,8))         #최소 공배수
'''로그'''
#print(log(4,2))             #a : 지수 / b : 밑
#print(log1p(e-1))           #밑이 e인 x+1로그
#print(log2(4))              #밑이 2인 x로그
#print(log10(100))           #밑이 10인 x로그
'''삼각함수'''
#print(sin(60))              #sin
#print(cos(60))              #cos
#print(tan(60))              #tan
#print(asin(2/3))            #아크sin
#print(acos(2/3))            #아크cos
#print(atan(2/3))            #아크tan
#print(atan2(60,60))         #아크tan x/y
'''각도 변환'''
#print(degrees(60))          #라디안 -> 60분법 각도
#print(radians(60))          #60분법 각도 -> 라디안
'''상수'''
#print(pi)                   #원주율
#print(e)                    #자연상수 e
#print(tau)                  #타우?
'''쓸모 없어 보임'''
#print(comb(1000,3))         #조합 / only 정수
#print(copysign(-3.14,2))    #x의 절대값 / y의 부호
#print(fabs(-30))            #x의 절대값 반환(float) - 근데 그냥 abs쓰셈
