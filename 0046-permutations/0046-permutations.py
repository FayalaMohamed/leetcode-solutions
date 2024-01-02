class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        if len(nums)==1:
            return [nums.copy()]

        for i in range(n):
            x = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms :
                perm.append(x)
            
            res.extend(perms)
            nums.append(x)

        return res




        """
        permut = []
        def backtrack(i: int):
            if len(permut) == n:
                res.append(permut.copy())
                return
            for k in range(n-i):
                permut.append(nums[(i+k) % n])
                backtrack(i+1)

                permut.pop()

        backtrack(0)
        return res
        """
            
