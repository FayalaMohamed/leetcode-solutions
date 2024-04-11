class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        q=len(nums)
        for i in range(len(nums)):
            b = nums[nums[i]]%q
            nums[i] = nums[i] + b*q
        for i in range(len(nums)):
            nums[i] = nums[i]/q
        return nums