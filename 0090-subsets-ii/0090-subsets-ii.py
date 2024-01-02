class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def backtracking( elements:  List[int], i: int):
            if i >= len(nums):
                return 
            

            elements.append(nums[i])
            res.append(elements.copy())
            backtracking(elements, i+1) # all the subsets found here will contain at least one nums[i]

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            elements.pop()
            backtracking(elements, i+1) # all the subsets found here will contain no nums[i]
            
        
        backtracking([], 0)
        return res