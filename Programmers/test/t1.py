def buy(n, battery, lst, result):
    count = (n // battery[0][0]) * battery[0][0]
    result += battery[0][1] * count // battery[0][0]

    lst.append(result + battery[0][1])

    if count == n: return result

    if len(battery) > 1:
        result = buy(n - count, battery[1:], lst, result)
    return result


def solution(n, battery):
    lst = []
    result = 0
    battery = sorted(battery, key=lambda x: x[1] / x[0])
    result = buy(n, battery, lst, result)
    lst.append(result)
    print(lst)

    return min(lst)