class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nbs = set()
        for x in nums:
            if x in nbs :
                return x
            nbs.add(x)