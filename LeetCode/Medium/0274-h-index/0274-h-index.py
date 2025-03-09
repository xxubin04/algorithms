class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n):
            if citations[i] >= n-i:
                return n-i
        return 0        