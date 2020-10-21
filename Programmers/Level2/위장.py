'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42578
'''
def solution(clothes):
    clothes_dict = {}
    for clothing, part in clothes:
        if part not in clothes_dict:
            clothes_dict[part] = [clothing]  # key : 옷종류 / value : [옷이름]
        else:
            clothes_dict[part].append(clothing)

    part_list = []
    answer = 1
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5)
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3)