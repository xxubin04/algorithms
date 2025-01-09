input = open(0).readline

S = set([])

for i in range(M := int(input())):
    command = list(input().strip().split())
    if command[0] == "add" and command[1] not in S:
        S.add(command[1])
    elif command[0] == "remove" and command[1] in S:
        S.remove(command[1])
    elif command[0] == "check":
        if command[1] in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        S = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif command[0] == "empty":
        S = set([])