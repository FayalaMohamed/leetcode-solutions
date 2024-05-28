class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        def dfs(pos, total):
            nonlocal cur
            if total == target:
                res.append(cur[:])
                return
            if pos>len(candidates)-1 or total > target:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                prev = candidates[i]
                dfs(i+1, total+candidates[i])
                cur.pop()
            
        dfs(0,0)
        return res
    