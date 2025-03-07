class Solution(object):
    def trailingZeroes(self, n):
        num = 1
        ans = 0
        for i in range(n, 0, -1):
            num *= i
        
        for j in reversed(list(str(num))):
            if j == '0':
                ans += 1
            else:
                return ans
