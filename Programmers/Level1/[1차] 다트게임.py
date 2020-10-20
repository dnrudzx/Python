'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17682
'''
def solution(dartResult):
    points = []
    point = ''
    for idx, i in enumerate(dartResult):
        point += i
        if i.isalpha():
            if idx != len(dartResult) - 1:
                if dartResult[idx + 1] == '*' or dartResult[idx + 1] == '#':
                    continue
                else:
                    points.append(point)
                    point = ''
            else:
                points.append(point)
        if i == '*' or i == '#':
            points.append(point)
            point = ''

    result_list = []
    for i in points:
        if i[1] == '0':
            if i[2] == 'S':
                result_list.append(int(i[:2]))
            elif i[2] == 'D':
                result_list.append(int(i[:2]) ** 2)
            else:
                result_list.append(int(i[:2]) ** 3)
        if i[1] == 'S':
            result_list.append(int(i[0]))
        elif i[1] == 'D':
            result_list.append(int(i[0]) ** 2)
        elif i[1] == 'T':
            result_list.append(int(i[0]) ** 3)

    for idx, i in enumerate(points):
        if len(i) == 3:
            if i[2] == '#':
                result_list[idx] *= -1
            elif i[2] == '*':
                result_list[idx] *= 2
                if idx != 0:
                    result_list[idx - 1] *= 2
        if len(i) == 4:
            if i[3] == '#':
                result_list[idx] *= -1
            else:
                result_list[idx] *= 2
                if idx != 0:
                    result_list[idx - 1] *= 2

    return sum(result_list)


print(solution(	"1S2D*3T") == 37)
print(solution("1D2S#10S") == 9)
print(solution(	"1D2S0T") == 3)
print(solution("1S*2T*3S") == 23)
print(solution("1D#2S*3S") == 5)
print(solution("1T2D3D#") == -4)
print(solution("1D2S3T*") == 59)