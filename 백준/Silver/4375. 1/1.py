import sys

while True:
    try:
        n = int(sys.stdin.readline())
        rem = 1 % n
        cnt = 1
        while rem != 0:  # 나머지가 0이 아니라면 (= 나누어떨어지지 않는다면)
            rem = (rem * 10 + 1) % n
            cnt += 1
        print(cnt)
    except:
        break