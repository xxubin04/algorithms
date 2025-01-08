input = open(0).readline

words = list(input().upper().strip())
alphabet = {}

for w in words:
    if w not in alphabet:
        alphabet[w] = 1
    else:
        alphabet[w] += 1

most_appear = sorted(alphabet.items(), key=lambda x: x[1])[-1]
if len(alpha_list := list(alphabet.values())) == 1:
    print(most_appear[0])
elif alpha_list.count(most_appear[1]) != 1:
    print("?")
else:
    print(most_appear[0])