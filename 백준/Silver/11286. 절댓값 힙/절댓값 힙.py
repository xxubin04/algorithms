from heapq import heappop, heappush, heapify
input = open(0).readline 

array = []

for i in range(N := int(input())):
    a = int(input())
    if a == 0 and array: print(heappop(array)[-1])
    elif a == 0 and not array:   print(0)
    else:
        heappush(array, (abs(a), a))