input = open(0).readline

channels = list()
for i in range(N := int(input())):
    channels.append(c := input().strip())

idx1, idx2 = channels.index("KBS1"), channels.index("KBS2")

button = ""

if idx1 > idx2:
    idx2 += 1

button += '1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1)
print(button)