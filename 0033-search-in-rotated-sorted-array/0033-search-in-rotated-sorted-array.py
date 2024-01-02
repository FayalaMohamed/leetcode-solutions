class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(left, right, pivot) :
            while left <= right:
                print(left, right)
                mid = left + (right - left) // 2
                if nums[(mid + pivot) % len(nums)] > target:
                    right = mid - 1
                elif nums[(mid + pivot) % len(nums)] < target:
                    left = mid + 1
                else:
                    return (mid + pivot) % len(nums)
            return -1
        pivot = nums.index(min(nums))
        left, right = 0, len(nums) - 1
        index = binarySearch(left, right, pivot)
        return index
        """
        mini = float('inf')
        minInd = 1
        for i,x in enumerate(nums):
            if x<mini:
                mini = x
                minInd = i
        rot =len(nums)-minInd

        l =0
        r= len(nums) 

        while l < r: 
            mid = (l+r)//2
            print((mid+rot)%len(nums))
            if nums[(mid+rot)%len(nums)] < target: 
                l = mid + 1
            elif nums[(mid+rot)%len(nums)] > target: 
                r = mid - 1
            else : 
                return (mid+rot)%len(nums)

        if l > 0 and nums[l -1] == target: 
            return l -1
        else:
            return -1
        """
