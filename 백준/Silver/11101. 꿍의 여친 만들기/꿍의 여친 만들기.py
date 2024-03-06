input = open(0).readline 

end = 1001
for i in range(n := int(input())):
    conditions = {}
    need = list(input().rstrip().split(','))
    for n in need:
        a, b = n.split(':')
        conditions[a] = int(b)
    cal1 = list(input().rstrip().split('|'))
    cal2 = []
    for j in cal1:
        cal2.append(nList := list(j.rstrip().split('&')))
    ans = []
    cal1 = [[] for _ in range(len(cal2))]
    for a in cal2:
        std = 0
        for b in range(len(a)):
            for k, v in conditions.items():
                if a[b] == k:
                    if v > std:
                        std = v
        ans.append(std)
    print(min(ans))