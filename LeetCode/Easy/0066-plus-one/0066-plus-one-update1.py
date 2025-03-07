class Solution(object):
    def plusOne(self, digits):
        digits = list(map(str, digits))
        num = int(''.join(digits)) + 1
        return list(map(int, list(str(num))))
