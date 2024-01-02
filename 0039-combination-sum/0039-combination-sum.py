class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nbs = [0]

        def backtracking(i: int):
            if i >= len(candidates):
                return
            
            added = False

            # if we can add the element we dadd it and update the first element of nbs 
            # which is the sum of the elements of the list
            if nbs[0] + candidates[i] <= target:
                nbs.append(candidates[i])
                nbs[0] = nbs[0] + candidates[i]
                added = True

                # if the sum is equal to the target we add the solution 
                # or we call backtracking for the same element we added
                if nbs[0] == target:
                    res.append(nbs[1:].copy())
                else:
                    backtracking(i)

            # if we added an element we remove it 
            # we call backtracking for the i+1 element
            if added :
                nbs.pop()
                nbs[0] = nbs[0] - candidates[i]
            
            backtracking(i+1)

        backtracking(0)
        return res