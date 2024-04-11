class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(2*len(nums))]
        
        for i in range(len(nums)):
            res[i]=nums[i]
            res[i+len(nums)] = nums[i]
            
        return res
        