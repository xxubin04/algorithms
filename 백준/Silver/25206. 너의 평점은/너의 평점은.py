total = 0
num = 0

scores = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    a, n, s = input().rstrip().split()
    if s != 'P':
        total += (scores[s] * float(n))
        num += float(n)

print(round(total / num, 6))