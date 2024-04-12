class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = {'a','e','i','o','u'}
        
        res, l, count = 0,0,0
        
        for i in range(len(s)):
            count += 1 if s[i] in vowel else 0
            if i-l+1>k:
                count -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res,count)
        return res
        