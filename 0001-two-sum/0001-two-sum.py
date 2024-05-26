class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        
        for i, x in enumerate(nums):
            toFind = target - x
            if toFind in myMap:
                return [myMap[toFind], i]
            myMap[x] = i
        