class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        i = 0
        while i < len(nums) - 3:
            l = i+1
            
            while l < len(nums)-2 :
                r = len(nums) - 1
                m = l+1
                while m<r:
                    x = nums[i] + nums[l] + nums[r] + nums[m]
                    if x == target:
                        res.append([nums[i],nums[l],nums[m],nums[r]])
                        while m<r and nums[m] == nums[m+1]:
                            m += 1
                        while m<r and nums[r] == nums[r-1]:
                            r -= 1
                        m += 1
                        r -= 1
                    elif x > target:
                        r -= 1
                    else:
                        m += 1
                while l < len(nums)-2 and nums[l+1] == nums[l]:
                    l += 1
                l += 1
            while i < len(nums)-3 and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return res