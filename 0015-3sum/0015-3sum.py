class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left < right :
                if(x+nums[left]+nums[right] == 0) :
                    res.append([x,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right :
                        left += 1
                elif(x+nums[left]+nums[right] > 0) :
                    right -= 1
                else :
                    left += 1
        return res


