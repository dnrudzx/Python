'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42583
'''
def solution(bridge_length, weight, truck_weights):
    time = 0
    ing_truck = []
    while truck_weights != []:
        if ing_truck == [] or weight >= sum([x[1] for x in ing_truck]) + truck_weights[0]:
            ing_truck.append((0,truck_weights[0]))
            truck_weights = truck_weights[1:]
        ing_truck = [(x+1,y) for x,y in ing_truck]
        time += 1
        if ing_truck != [] and ing_truck[0][0] == bridge_length:
            ing_truck = ing_truck[1:]
    return time+bridge_length


print(solution(2, 10, [7, 4, 5, 6]) == 8)
print(solution(100, 100, [10]) == 101)
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)