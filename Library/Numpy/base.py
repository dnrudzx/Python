'''
numpy : 파이썬에서 배열하면 제일 먼저 생각나는 라이브러리
    파이선은 기본적으로 배열이라는 구조체가 없는데 이걸 제공해줌
    배열에 대한 강력한 기능들을 제공한다
'''
import numpy as np

'''1. Array 정의'''
#1.1 단순 생성
data_1 = np.array([1,2,3,4,5])
data_2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#1.2 0으로 구성된 배열
data_zero_1 = np.zeros(10)
data_zero_2 = np.zeros((3,5))
#1.3 1로 구성된 배열
data_one_1 = np.ones(10)
data_one_2 = np.ones((3,5))
#1.4 범위로 구성된 배열
data_arange_1 = np.arange(10)
data_arange_2 = np.arange(3,10)
#1.5 렌덤값으로 구성된 배열
#print(data_random = np.random.randn(5,3))        #보통 이걸로 씀
#print(np.random.random((5,3)))     #0<x<1 범위 / 파라미터가 size
#print(np.random.rand(5,3))         #2번째와 같음 / 파라미터가 차이
data_random = np.random.randn(5,3)

'''2. Array 구성'''
#2.1 형태 확인 : (행, 열)
#print(data_1.shape)
#2.2 자료형 확인
#print(data_1.dtype)


'''3. Array 연산'''
arr1 = np.array([[1,2,3],[4,5,6]])
#3.1 사칙연산 + 나머지연산 + 몫연산 + 제곱연산
#print(arr1 + 2)
#print(arr1 - 2)
#print(arr1 * 2)
#print(arr1 / 2)
#print(arr1 % 2)
#print(arr1 // 2)
#print(arr1 ** 2)
#3.2 배열간 사칙연산(shape가 같은 경우에만 가능) + 나머지연산 , 몫연산, 제곱연산 가능
    #각 요소들 끼리만 연산이 된다
#print(data_one_1 + data_zero_1)
#print(data_one_1 - data_zero_1)
#print(data_one_1 * data_zero_1)
#print(data_zero_1 / data_one_1)
#print(data_zero_1 // data_one_1)
#print(data_one_1 % data_one_1)
#print(data_one_1 ** data_zero_1)
#3.3 브로드캐스트 : 크기가 서로 다른 array끼리 연산 가능
    #열은 맞춰줘야한다
#arr2 = np.array([10,11,12])
#print(arr1 + arr2)


'''4. Array 인덱싱'''
#4.1 기본 : 똑같음
#4.2 마스크 : 어디에 쓰이는지는 모르겠음
'''
data = np.array([1,2,1,2,1,2])      #배열 생성
data2 = np.array([1,2,3,4,5,6])
data_mask = (data == 1)             #벼열에서 1인건 True 아닌건 False
print(data_mask)                    #[ True False  True False  True False]
print(data2[data_mask])             #True인 인덱스에 대한 값 표시
print(data2[data==1])               #이렇게도 표시 가능
print(data2[(data==1) | (data==2)]) #논리연산 가능(and -> &, or -> |)
'''


'''5. 기타 함수'''
#print(np.abs(data_random))         #절대값
#print(np.sqrt(data_random))        #제곱근 계산
#print(np.square(data_random))      #제곱 계산
#print(np.exp(data_random))         #무리수 e의 지수로 삼은 값 계산
#print(np.log(data_random))         #자연로그 : 밑이 e인 로그
#print(np.log10(data_random))       #상용로그 : 밑이 10인 로그
#print(np.log2(data_random))        #밑이 2인 로그
#print(np.sign(data_random))        #부호 계산(+,-)
#print(np.ceil(data_random))        #소수 첫번째 자리에서 올림
#print(np.floor(data_random))       #소수 첫번째 자리에서 내림
#print(np.isnan(data_random))       #값이 nan이면 True 아니면 False
#print(np.isinf(data_random))       #값이 무한대면 Ttre 아니면 False
