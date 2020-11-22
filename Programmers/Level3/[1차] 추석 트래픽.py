'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17676
'''
def check(start, end, lst):
    num = 0
    for j in lst:
        if not (j[1] < start or j[0] > end):
            num += 1
    return num
def solution(lines):
    answer = []
    lst = []
    import datetime
    for line in lines:
        log = line.split(' ')
        end = start = datetime.datetime.strptime(log[0]+log[1]+'000', '%Y-%m-%d%H:%M:%S.%f')
        T = float(log[2][:-1]) * 1000000 - 1000
        start = end - datetime.timedelta(microseconds=int(T))
        lst.append([start, end])
    for i in lst:
        start_1 = i[0]
        start_2 = i[1]
        end_1 = start_1 + datetime.timedelta(microseconds=1000)
        end_2 = start_2 + datetime.timedelta(microseconds=1000)

        answer.append(check(start_1,end_1,lst))
        answer.append(check(start_2, end_2, lst))

    return max(answer)

print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
