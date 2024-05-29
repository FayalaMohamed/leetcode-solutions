class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                dp[i] = max(dp[j]+1, dp[i]) if nums[i] < nums[j] else dp[i]
        
        return max(dp)