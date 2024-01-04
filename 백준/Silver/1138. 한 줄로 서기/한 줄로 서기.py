input = open(0).readline

people = int(input())
dic = {}; ans = [0 for _ in range(people)]

tallNum = list(map(int, input().split()))
for j in range(people):
    dic[j+1] = tallNum[j]

for i in sorted(dic, reverse=True):
    if ans[dic[i]] != 0:
        p = -1
        while p != people * (-1) + dic[i]:
            ans[p] = ans[p-1]
            ans[p-1] = 0
            p -= 1
    ans[dic[i]] = i

for a in ans:
    print(a, end=" ")