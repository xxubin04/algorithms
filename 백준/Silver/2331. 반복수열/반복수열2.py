A, P = map(int, input().split())
visited = {A:1}
ans = 0

def recursion(x):
    global ans
    digit = [i for i in list(map(int, str(x)))]
    num = sum(j**P for j in digit)
    if num not in visited:
        visited[num] = 1
        recursion(num)
    else:
        visited[num] += 1
        for v in visited.values():
            if v != 2:
                ans += 1
            else:
                break

    return ans

print(recursion(A))
