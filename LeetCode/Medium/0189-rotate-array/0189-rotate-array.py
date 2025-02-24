class Solution(object):
    def rotate(self, nums, k):
        shift = nums[:-k] 
        del nums[:-k]
        nums.extend(shift)