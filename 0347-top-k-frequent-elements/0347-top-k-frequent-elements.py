class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nbs = [[] for i in range(len(nums)+1)] 
        count = defaultdict(int)
        
        for x in nums:
            count[x] += 1
        for x, c in count.items():
            nbs[c].append(x)
        
        res = []
        for i in range(len(nbs)-1,-1,-1):
            for x in nbs[i]:
                res.append(x)
                k-=1
                if k==0:
                    return res
        
            
        