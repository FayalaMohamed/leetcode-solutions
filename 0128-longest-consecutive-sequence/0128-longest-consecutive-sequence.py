class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mySet = set(nums)
        res = 0
        for num in mySet :
            if num-1 not in mySet:
                nextNum = num +1 
                while(nextNum in mySet):
                    nextNum = nextNum + 1
                res = max(res,nextNum-num)
        return res
            
