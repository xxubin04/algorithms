class Solution(object):
    def wordPattern(self, pattern, s):
        dictionary = {}
        words = list(s.split())

        if len(words) != len(pattern):
            return False

        for p in range(len(pattern)):  
            if not pattern[p] in dictionary.keys() and not words[p] in dictionary.values():
                dictionary[pattern[p]] = words[p]
            elif not pattern[p] in dictionary.keys() and words[p] in dictionary.values():
                return False
            elif words[p] != dictionary[pattern[p]]:
                return False
        
        return True 
        