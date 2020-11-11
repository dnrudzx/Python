'''
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42626
'''
def solution(scoville, K):
    answer = 0

    import heapq
    heapq.heapify(scoville)

    if K <= scoville[0]: return 0
    while True:
        if scoville[0] >= K: return answer
        if len(scoville) < 2: return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        new = a + 2 * b
        if new <= 0: return -1
        answer += 1
        heapq.heappush(scoville, new)

print(solution([1, 2, 3, 9, 10, 12], 7) == 2)