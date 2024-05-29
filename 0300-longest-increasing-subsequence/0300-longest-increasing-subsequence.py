class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0,i):
                dp[i] = max(dp[j]+1, dp[i]) if nums[i] > nums[j] else dp[i]
        
        return max(dp)