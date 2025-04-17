input = open(0).readline

i = 1

while True:
    L, P, V = map(int, input().split())
    
    if (L + P + V) == 0:
        break

    if (V % P) >= L:
        print(f"Case {i}: {L * (V // P) + L}")
    else:
        print(f"Case {i}: {L * (V // P) + (V % P)}")
    i += 1
