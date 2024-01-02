class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chars = {}
        maxi = 0
        maxChar = 0
        l = 0
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            maxChar = max(maxChar, chars[s[r]])

            while (r-l+1) - maxChar > k:
                chars[s[l]] -= 1
                l += 1
            maxi = max(maxi, r-l+1)
        return maxi

