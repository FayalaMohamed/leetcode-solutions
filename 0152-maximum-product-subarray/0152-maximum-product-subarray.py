class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mini, maxi = 1, 1

        for x in nums:
            tmp = mini * x
            mini = min(mini*x, maxi*x, x)
            maxi = max(tmp, maxi*x, x)
            res = max(res, maxi)
        return res