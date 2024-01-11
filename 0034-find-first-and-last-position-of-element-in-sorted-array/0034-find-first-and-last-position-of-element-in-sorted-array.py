class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        i = 0
        while i<len(nums):
            if nums[i]==target and res[0]==-1:
                res[0] = i
            if nums[i]==target and res[0]!=-1 :
                res[1] = i
            i+=1
        return res
        