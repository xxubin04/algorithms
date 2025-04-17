N = int(input())
arr = [5*i for i in range(N // 5, -1, -1)]  # 5킬로그램 봉지로 배달할 수 있는 무게 리스트 

for j in range(len(arr)):
    if (div := N - arr[j]) == 0:  # 5킬로그램 봉지로 배달하고 나머지 설탕이 없다면 
        print(len(arr) - j - 1)  
        quit()
    elif div % 3 == 0:  # 나머지 설탕이 3킬로그램 봉지로 딱 나눠떨어진다면 
        print((len(arr) - j - 1) + (div // 3))
        quit()

print(-1)  # 나눠떨어지지 않는다면 -1 출력 
