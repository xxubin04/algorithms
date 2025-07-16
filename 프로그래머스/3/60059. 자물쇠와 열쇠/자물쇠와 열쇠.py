def rotate_90(key):
    l = len(key)
    return [[key[l - j - 1][i] for j in range(l)] for i in range(l)]

def solution(key, lock):
    l = len(key)
    n = len(lock)
    size = n + 2 * (l - 1)

    for _ in range(4):
        key = rotate_90(key)

        for x in range(size - l + 1):
            for y in range(size - l + 1):
                padding = [[0] * size for _ in range(size)]

                for i in range(n):
                    for j in range(n):
                        padding[i + l - 1][j + l - 1] = lock[i][j]

                for i in range(l):
                    for j in range(l):
                        padding[x + i][y + j] += key[i][j]

                unlock = True
                for i in range(n):
                    for j in range(n):
                        if padding[i + l - 1][j + l - 1] != 1:
                            unlock = False
                            break
                    if not unlock:
                        break

                if unlock:
                    return True

    return False