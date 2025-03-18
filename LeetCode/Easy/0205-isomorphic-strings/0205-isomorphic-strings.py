class Solution(object):
    def isIsomorphic(self, s, t):
        isomorphic_dict = {}
        s_list = list(s)

        prior = s_list[0]

        for i in range(len(s_list)):
            if not s_list[i] in isomorphic_dict.keys():
                if t[i] in isomorphic_dict.values():
                    return False
                isomorphic_dict[s_list[i]] = t[i]
            elif isomorphic_dict[s_list[i]] != t[i]:
                return False
            
        return True 
        