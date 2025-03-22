class Solution(object):
    def isAnagram(self, s, t):
        s_dict = list(s)
        t_dict = list(t)

        if len(s) != len(t):
            return False
            
        for i in t_dict:
            if not i in s_dict:
                return False

        for j in s_dict:
            if not j in t_dict:
                return False

        return True