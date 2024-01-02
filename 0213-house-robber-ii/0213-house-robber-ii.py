class Solution(object):
    def rob1(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        nums[1] =  max(nums[0], nums[1])
                
        for i in range(2, len(nums)):
            # either i rob the current one and take what i robbed in the previous one (not the adjacent)
            # or dont rob the current and just take what i robbed so far in the adjacent one
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])

        return nums[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]), nums[0])