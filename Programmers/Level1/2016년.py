'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12901
'''
def solution(a, b):
    import datetime
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.date(2016,a,b).weekday()
    return answer[day]


print(solution(5, 24) == 'TUE')