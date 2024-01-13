A, P = map(int, input().split())
visited = {A:1}

while 1:
    digit = [i**P for i in list(map(int, str(A)))]
    A = sum(digit)
    if A not in visited:
        visited[A] = 1
    elif visited[A] == 2:
        break
    else:
        visited[A] += 1

ans = sum(value==1 for value in visited.values())
print(ans)