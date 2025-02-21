class Solution(object):
    def removeElement(self, nums, val):
        for n in range(len(nums)-1, -1, -1):
            if nums[n] == val:
                nums.pop(n)
