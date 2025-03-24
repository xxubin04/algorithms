class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_list = list(ransomNote)
        m_list = list(magazine)
        prior_idx = 0
        words = []

        for idx in range(len(ransomNote)):
            if r_list[prior_idx] != r_list[idx]:
                words.append(ransomNote[prior_idx:idx])
                prior_idx = idx
            
        words.append(ransomNote[prior_idx:idx+1])

        ans = [1] * len(words)

        for w in range(len(words)):
            for i in range(len(magazine) - len(words[w]) + 1):
                if words[w] == ''.join(m_list[i:i+len(words[w])]):
                    ans[w] = 0
                    break

        if sum(ans) == 0:
            return True
        else:
            return False