class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        lowest = prices[0]
        for x in prices:
            if x<lowest:
                lowest = x
            res = max(res, x-lowest)
        return res

