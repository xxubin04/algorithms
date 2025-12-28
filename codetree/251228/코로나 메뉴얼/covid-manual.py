import sys
cnt = 0

for _ in range(3):
    symptom, temp = sys.stdin.readline().split()
    if symptom == 'Y':
        if int(temp) >= 37:
            cnt += 1

print('E' if cnt >= 2 else 'N')