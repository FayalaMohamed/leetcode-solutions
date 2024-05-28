class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        def dfs(i, total):
            nonlocal cur
            if total == target:
                res.append(cur[:])
                return
            if i>len(candidates)-1 or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i+1, total + candidates[i])
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            cur.pop()
            dfs(i+1, total)
            
        dfs(0,0)
        return res
    