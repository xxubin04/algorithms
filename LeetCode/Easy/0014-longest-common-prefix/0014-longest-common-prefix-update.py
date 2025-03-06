class Solution(object):
    def longestCommonPrefix(self, strs):
        word = ""
        target = ""
        for i in range(len(strs[0])):
            target += strs[0][i]
            for j in strs[1:]:
                if j[:i+1] != target:
                    return word
            word = target
        return word
