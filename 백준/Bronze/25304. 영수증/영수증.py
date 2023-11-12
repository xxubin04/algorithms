total = int(input())
num = int(input())
bill = 0
for i in range(num):
    a, b = map(int, input().split())
    bill += a*b
if total == bill:
    print("Yes")
else:
    print("No")