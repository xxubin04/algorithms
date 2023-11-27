from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    array = {}
    line = stdin.readline().split()
    N = int(line[0])
    max_val = 0
    max_key = 0
    for i in range(1, len(line)):
        num = int(line[i])
        if num not in array:
            array[num] = 1
        else:
            array[num] += 1
        if array[num] > max_val:
            max_val = array[num]
            max_key = num
    if max_val > N / 2:
        
        print(max_key)
    else:
        print('SYJKGW')