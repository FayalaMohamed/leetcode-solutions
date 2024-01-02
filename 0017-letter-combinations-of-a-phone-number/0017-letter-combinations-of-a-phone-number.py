class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        

        def  backtrack(i: int, curr: str):
            if i >= len(digits):
                res.append(curr)
                return
            for c in chars[digits[i]]:
                curr = curr + c
                backtrack(i+1, curr )
                curr = curr[:len(curr)-1]
        
        if digits:
            backtrack(0, "")
        return res