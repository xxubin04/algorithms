class Solution(object):
    def isValid(self, s):
        word = []
        for i in list(s):
            if i in "([{":
                word.append(i)
            elif i in ")]}":
                if not word or not word.pop()+i in ["()", "[]", "{}"]:
                    return False
        if not word: return True
  