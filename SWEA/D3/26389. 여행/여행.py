T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''

    A = input().strip()

    n = A.count('N')
    s = A.count('S')
    e = A.count('E')
    w = A.count('W')

    possible = True
    if (n != 0 and s == 0) or (n == 0 and s != 0):
        possible = False

    if (w != 0 and e == 0) or (w == 0 and e != 0):
        possible = False

    print("Yes" if possible else "No")