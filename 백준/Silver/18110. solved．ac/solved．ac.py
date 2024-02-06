input = open(0).readline

def round2(a):
    return int(a) + (1 if a - int(a) >= 0.5 else 0)

num = []
for i in range(N := int(input())):
    num.append(int(input()))

if N == 0:
    print(0)
else:
    print(round2(sum(sorted(num)[round2(N*0.15) : N-round2(N*0.15)])/(N-(2*round2(N*0.15)))))