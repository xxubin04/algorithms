# class Solution(object):
#     def isPalindrome(self, s):
#         s_list = list(s)
#         word = ""
#         reversed_word = ""
#         for i in range(len(s_list)):
#             if s_list[i].isupper():
#                 word += s_list[i].lower()
#             elif s_list[i].isalpha() or s_list[i].isdigit():
#                 word += s_list[i]
#         for j in reversed(list(word)):
#             reversed_word += j
#         if word == reversed_word:
#             return True
#         return False             



from collections import deque

class Solution(object):
    def isPalindrome(self, s):
        ans = deque()
        s_list = list(s)
        for i in s_list:
            if i.isalnum():
                ans.append(i.lower())
        if ''.join(ans) ==  ''.join(reversed(ans)):
            return True
        return False