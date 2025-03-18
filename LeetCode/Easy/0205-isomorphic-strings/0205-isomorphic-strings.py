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
            
        # isomorphic_dict = {}
        # s_list = list(s)

        # prior = s_list[0]

        # for i in range(len(s_list)):
        #     if not s_list[i] in isomorphic_dict.keys():
        #         if t[i] in isomorphic_dict.values():
        #             return False
        #         isomorphic_dict[s_list[i]] = t[i]
        #     elif isomorphic_dict[s_list[i]] != t[i]:
        #         return False
            
        # return True 
        