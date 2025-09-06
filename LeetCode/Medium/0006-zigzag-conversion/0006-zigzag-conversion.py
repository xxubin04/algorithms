class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        nums = [[] for _ in range(numRows)]
        
        rev = False

        if numRows == 1:
            return s
        
        idx = 0
        for c in s:
            nums[idx].append(c)

            if not rev:
                idx += 1
            else:
                idx -= 1
            
            if idx == numRows - 1:
                rev = True
            elif idx == 0:
                rev = False
        
        for n in nums:
            t = "".join(n)
            ans += t
        
        return ans
    