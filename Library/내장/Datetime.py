'''
datetime : 날짜와 시간을 조작하는 클래스 제공
    달력관련 : calendar
    시간 액세스 : time
    시간대와 구문 분석 지원 확장 : dateutil
'''
import datetime

#현재 날짜와 시간 : 연/월/일 시/분/초/마이크로초
print(datetime.datetime.today())

#데이터 -> 객체
data = datetime.datetime(2018,5,19,3,50,50,111)
print(data)
#문자열 -> 객체
string = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')
print(type(string))

#객체 -> 데이터(각각 Y/m/d/H/M/S/f : 대소문자 주의(개빡침))
data = data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond
print(data)
#객체 -> 문자열
string = string.strftime('%Y-%m-%d')
print(type(string))

#시간 산술
day = datetime.datetime.today()
print(day - datetime.timedelta(days=20))
print(day - datetime.timedelta(hours=1))
print(day - datetime.timedelta(minutes=10))
print(day - datetime.timedelta(seconds=30))
print(day - datetime.timedelta(microseconds=20))
print(day)

#시간간 관계 가능
a = "2016-09-15 00:00:00:000000 3s"
a = datetime.datetime.strptime(a[:-3], '%Y-%m-%d %H:%M:%S:%f')
b = "2016-09-16 00:00:00:000000 3s"
b = datetime.datetime.strptime(b[:-3], '%Y-%m-%d %H:%M:%S:%f')
c = "2016-09-15 01:00:00:000000 3s"
c = datetime.datetime.strptime(c[:-3], '%Y-%m-%d %H:%M:%S:%f')
if c > a and c < b:
    print(True)