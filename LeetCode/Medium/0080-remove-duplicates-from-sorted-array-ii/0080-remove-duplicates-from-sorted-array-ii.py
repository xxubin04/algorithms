class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(2, len(nums)):
            if nums[j] != nums[i]:
                nums[i+2] = nums[j] 
                i += 1
        nums[i+2:] = []