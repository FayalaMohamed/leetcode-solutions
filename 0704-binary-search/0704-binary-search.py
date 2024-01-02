class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l =0
        r= len(nums)


        while l < r: 
            mid = (l+r)//2
            if nums[mid] <= target: 
                l = mid + 1
            else:
                r = mid

        if l > 0 and nums[l -1] == target: 
            return l -1
        
        else:
            return -1
            
        """
        if len(nums) == 1 and nums[0]!=target:
            return -1 
        if len(nums) == 1 and nums[0]==target:
            return 0
        i = 0
        j = len(nums) - 1
        k = len(nums)//2
        while i < j :
            if j == i+1 and nums[i]==target:
                return i
            elif j == i+1 and nums[j]==target:
                return j
            elif j == i+1 :
                return -1

            if nums[k] == target :
                return k
            if nums[k] > target :
                j = k
                k = (i+j)//2
            else :
                i = k
                k = (i+j)//2
        return -1
        """

