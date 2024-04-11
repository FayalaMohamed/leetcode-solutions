class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lcount, rcount = 0,0
        last = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<last:
                last = nums[i]
            else:
                rcount += 1
                
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>last:
                last = nums[i]
            else:
                lcount += 1
                
        return min(lcount,rcount)<=1
            
        