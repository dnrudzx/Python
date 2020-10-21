'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42577
'''
def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x:len(x))
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]) == False)
print(solution(	["123", "456", "789"]) == True)
print(solution(["12", "123", "1235", "567", "88"]) == False)