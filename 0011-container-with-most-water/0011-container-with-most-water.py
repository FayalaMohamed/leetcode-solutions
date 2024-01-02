class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxi=0
        while left < right :
            area = (right-left)*min(height[left], height[right])
            if area > maxi:
                maxi = area
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
        return maxi
