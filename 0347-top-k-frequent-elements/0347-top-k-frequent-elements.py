class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniqueElems = set(nums)
        counts = {}
        for i in uniqueElems:
            counts[i]=nums.count(i)
        sorted_counts = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))
        return list(sorted_counts.keys())[:k]


