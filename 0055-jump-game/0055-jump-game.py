class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        
        for i in range(len(nums)-1):
            if maxIndex<i:
                return False
            if i+nums[i]>maxIndex:
                maxIndex = i +nums[i]
            if maxIndex>=len(nums)-1:
                return True
        return maxIndex >= len(nums)-1