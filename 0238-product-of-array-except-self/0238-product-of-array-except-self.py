class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postProd = [1] * (len(nums))
        preProd = [1] * (len(nums))
        res = [1] * (len(nums))
        for i in range(1,len(nums)):
            preProd[i]=preProd[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            postProd[i]=postProd[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=postProd[i]*preProd[i]
        return res


