from heapq import heappop, heappush, heapify
input = open(0).readline 

array = []
heapify(array)

for i in range(N := int(input())):
    if (x := int(input())) != 0:
        heappush(array, x) 
    else:
        if len(array) == 0:
            print(0)
        else:
            print(heappop(array))