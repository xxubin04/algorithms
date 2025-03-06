class Solution(object):
    def longestCommonPrefix(self, strs):
        word = ""
        target = ""
        strs.sort(key=len)  # update: 기준 문자열을 길이가 가장 짧은 문자열로 설정 
        for i in range(len(strs[0])):
            target += strs[0][i]
            for j in strs[1:]:
                if j[:i+1] != target:
                    return word
            word = target
        return word
