class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        itemset=set()
        for i in nums:
            if(i in itemset):
                return True
            itemset.add(i)
        return False
