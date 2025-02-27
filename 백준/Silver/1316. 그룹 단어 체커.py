cnt = 0
for _ in range(int(input())):
    word = list(input().rstrip())
    flag = True
    prior = word[0]
    appear = []
    for w in word:
        if w in appear and prior != w:
            flag = False
        elif not w in appear:
            appear.append(w)
            prior = w
    if flag:
        cnt += 1
print(cnt)