class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        perm = []
        
        dic = defaultdict(int)
        for x in nums:
            dic[x] += 1
            
        def dfs():
            if len(perm)==len(nums):
                res.append(list(perm))
                return
            for x in dic:
                if dic[x]>0:
                    dic[x]-=1
                    perm.append(x)
                    dfs()
                    perm.pop()
                    dic[x]+=1
        dfs()
        return res
        