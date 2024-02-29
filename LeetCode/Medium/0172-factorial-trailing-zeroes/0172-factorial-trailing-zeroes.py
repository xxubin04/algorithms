class Solution(object):
    def trailingZeroes(self, n):
        if n in [0, 1]:
            return 0
        total = 1
        while n >= 2:
            total *= n
            n -= 1
        cnt = 0
        for i in reversed(list(str(total))):
            if i == '0':
                cnt += 1
            else:
                break
        return cnt