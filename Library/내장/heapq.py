'''
heapq : 이진트리 기반의 최소힙(min heap) 자료구조제공
    - 원소들이 항상 정렬된 상태로 추가/삭제
    - 가장 작은값은 언제나 인덱스 0(루트)
    - 모든 원소(k)는 항상 자식원소(2k+1, 2k+2)보다 작거나 같다
'''
'''
import heapq

#최소 힙 생성 : 리스트와 같은 자료구조를 가지고, heapq.heappush명령어로 추가해야함
heap = []
#원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
#가장 작은값 꺼내기
print(heap[0])              #힙의 루트노드는 가장 작은 값이다
                                #주의 : 루트노드는 가장 작은 값이지만, 인덱스 1의 값이 두번째로 작은 값이란 보장은 없다
print(heapq.heappop(heap))  #루트노드 꺼내기
#기존 리스트 - 힙변환
lst = [4,1,7,3,8,5]
heapq.heapify(lst)
print(lst)
'''
'''응용 1: 최대힙 만들기'''
'''
nums = [4,1,7,3,8,5]
heap = []
for num in nums:
    heapq.heappush(heap, (-num, num))

while heap:
    print(heapq.heappop(heap)[1])
'''
'''응용2 : 힙 정렬
        일반적인 sorted함수 : n^2
        heap : nlgn'''
'''
def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums
print(heap_sort([4, 1, 7, 3, 8, 5]))
'''
'''응용3 : 순서구하기(정렬 효율성 높음)'''
'''
def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min
print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

'''