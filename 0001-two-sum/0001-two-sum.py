class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        i = 0
        j = 1
        while i != length :
            while j != length :
                if nums[i]+nums[j] == target :
                    return(i,j)
                else:
                    j += 1
            i += 1
            j = i+1
