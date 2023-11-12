dishes = int(input())
potato = list(map(int, input().split()))

potato.sort()

low = sum(potato[:int(len(potato)/2)])
print(low, sum(potato)-low)