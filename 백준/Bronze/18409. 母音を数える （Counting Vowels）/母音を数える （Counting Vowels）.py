vowel = ['a','e','i','o','u']
ans = 0
n = int(input()); A = list(input())
for i in A:
    if i in vowel: ans += 1
    else: pass
print(ans)