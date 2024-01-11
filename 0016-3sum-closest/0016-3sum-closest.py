class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float("inf")
        nums.sort()
        
        i = 0
        while i < len(nums)-2:
            left , right = i+1 , len(nums)-1
            
            while left<right:
                x = nums[i] + nums[left] + nums[right]
                if abs(x-target)<abs(res-target):
                    res = x
                if x < target:
                    left += 1
                elif x > target:
                    right -= 1
                else:
                    return res
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
        
        return res
        