class Solution(object):
    def isSubsequence(self, s, t):
        seq = []

        for i in (list(s)):
            for idx, element in enumerate(list(t)):
                if i == element and not idx in seq:
                    seq.append(idx)

        if seq == sorted(seq) and len(seq) == len(s):
            return True
        else:
            return False