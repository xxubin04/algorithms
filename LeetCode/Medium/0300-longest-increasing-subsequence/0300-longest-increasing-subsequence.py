class Solution(object):
    def lengthOfLIS(self, nums):
        cnt = [1] * len(nums)
        
        for std in range(len(nums)):
            for idx in range(std):
                if nums[idx] < nums[std]:
                    cnt[std] = max(cnt[std], cnt[idx]+1)

        return max(cnt)