class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome (s: str):
            i ,j = 0, len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(i: int):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()

        backtrack(0)
        return res