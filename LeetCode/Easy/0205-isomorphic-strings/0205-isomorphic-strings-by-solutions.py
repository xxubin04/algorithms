class Solution(object):
    def isIsomorphic(self, s, t):
        s_index = {}
        t_index = {}

        for i in range(len(s)):
            if not s[i] in s_index.keys():
                s_index[s[i]] = i
                
            if not t[i] in t_index.keys():
                t_index[t[i]] = i

            if s_index[s[i]] != t_index[t[i]]:
                return False

        return True 
