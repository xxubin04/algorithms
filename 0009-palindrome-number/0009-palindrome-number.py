class Solution(object):
    def isPalindrome(self, x):
        word = list(str(x))
        for i in range(len(word)//2+1):
            if word[i] == word[-(i+1)]:
                continue
            else:
                return False
        return True