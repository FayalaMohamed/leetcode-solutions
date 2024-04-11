class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i+n]
            
        j= 2*n-1
        for i in range(n-1,-1,-1):
            nums[j] = nums[i]&1023
            nums[j-1] = nums[i]>>10
            j -= 2
        return nums