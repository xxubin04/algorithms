class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        for j in range(len(nums)):
            if j > 0 and nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        nums[i:] = []