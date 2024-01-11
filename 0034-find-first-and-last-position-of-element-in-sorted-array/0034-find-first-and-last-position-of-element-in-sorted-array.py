class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """res = [-1, -1]
        i = 0
        while i<len(nums):
            if nums[i]==target and res[0]==-1:
                res[0] = i
            if nums[i]==target and res[0]!=-1 :
                res[1] = i
            i+=1
        return res"""
        
        def find_first(nums, target):
            start = 0
            end = len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] == target:
                    first = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return first
        def find_last(nums, target):
            start = 0
            end = len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] == target:
                    start = mid + 1
                    last = mid
                else:
                    start = mid + 1
            return last
        return [find_first(nums, target), find_last(nums, target)]