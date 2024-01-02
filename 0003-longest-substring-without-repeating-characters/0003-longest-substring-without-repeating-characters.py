class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        maxi = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char in chars :
                maxi = max(maxi, len(chars))
                i = chars[char] + 1
                chars = {}
            else:
                chars[char]=i
                i += 1
        maxi = max(maxi, len(chars))
        return maxi