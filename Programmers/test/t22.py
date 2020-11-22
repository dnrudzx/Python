lst = []
def make_case(n, battery, price,check):
    global lst
    if check:return lst
    k = (n // battery[0][0]) * battery[0][0]
    price += battery[0][1] * k // battery[0][0]

    if k == n:
        lst.append(price)
        #check = True
        return lst
    lst.append(price + battery[0][1])
    if k != 0:
        for i in range(n - k, n, battery[0][0]):
            lst = make_case(i, battery[1:], price,check)
    else:
        lst = make_case(n, battery[1:],price,check)


def solution(n, battery):
    answer = 0
    battery = sorted(battery, key=lambda x: x[1] / x[0])
    cases = make_case(n, battery, 0,False)
    print(cases)

    return answer

print(solution(	50, [[10, 100000], [4, 35000], [1, 15000]]))