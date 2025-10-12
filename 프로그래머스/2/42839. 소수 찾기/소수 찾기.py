perm = []

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True 
    
def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    
    def generate(chosen, used):
        if len(chosen) == r and (num := int(''.join(chosen))) not in perm:
            if num == 0 or num == 1:
                return 
            
            if is_prime(num):
                perm.append(num)
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

def solution(numbers):
    for r in range(1, len(numbers)+1):
        permutation(list(numbers), r)
    
    return len(perm)