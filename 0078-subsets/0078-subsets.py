class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtracking( elements:  List[int], i: int):
            if i >= len(nums):

                return 
            
            elements.append(nums[i])
            res.append(elements.copy())
            backtracking(elements, i+1)

            elements.pop()
            backtracking(elements, i+1)
            
        
        backtracking([], 0)
        return res
