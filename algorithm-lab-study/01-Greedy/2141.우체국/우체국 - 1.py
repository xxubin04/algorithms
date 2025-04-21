towns = {}

for _ in range(N := int(input())):
    town, people = map(int, input().split())
    towns[town] = people

towns = sorted(towns.items(), key=lambda x: x[0])

total = 0
total_people = sum(towns[j][1] for j in range(N))

for i in range(N):  # 우체국 위치
    total += towns[i][1]
    if total >= (total_people + 1) // 2:
        print(towns[i][0])
        break
