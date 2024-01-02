class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        maxLen = 0

        palind = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            palind[i][i] = True
            maxLen = 1
            res = s[i:i+1]

        for i in range(0, len(s)-1):
            if s[i]==s[i+1] :
                palind[i][i+1] = True
                res = s[i:i+2]
                maxLen = 2 
        
        for i in range(3, len(s)+1):
            for j in range(0, len(s)-i+1):
                palind[j][j+i-1] = (palind[j+1][j+i-2] and (s[j]==s[j+i-1] ))
                if i > maxLen and palind[j][j+i-1]:
                    res = s[j:j+i]
                    maxLen = i

        return res
        
