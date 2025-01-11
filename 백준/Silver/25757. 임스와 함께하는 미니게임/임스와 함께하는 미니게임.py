input = open(0).readline

people = {'Y': 1, 'F': 2, 'O': 3}  # 게임의 종류에 따른 참가 인원수
participant = []  # 사람들의 이름 저장
N, game = input().strip().split()
for _ in range(int(N)):
    participant.append(input().strip())

participant = set(participant)
print(int(len(participant)/people[game]))