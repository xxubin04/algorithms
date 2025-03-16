class Solution(object):
    def addBinary(self, a, b):
        A, B = int(a, 2), int(b, 2)
        return bin(A+B)[2:]
        