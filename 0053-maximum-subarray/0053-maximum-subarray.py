class Solution:
    def maxCrossingSum(self, nums, left, mid, right):
        # Include elements on the left of mid
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            if current_sum > left_sum:
                left_sum = current_sum

        # Include elements on the right of mid
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            if current_sum > right_sum:
                right_sum = current_sum

        # Return sum of elements on left and right of mid
        return left_sum + right_sum

    def maxSubArraySum(self, nums, left, right):
        # Base case: only one element
        if left == right:
            return nums[left]

        # Find the middle point
        mid = (left + right) // 2

        # Recursively find the maximum sum in left, right, and crossing mid
        maxLeft = self.maxSubArraySum(nums, left, mid)
        maxRight = self.maxSubArraySum(nums, mid + 1, right)
        maxCross = self.maxCrossingSum(nums, left, mid, right)

        # Return the maximum of the three
        return max(maxLeft, maxRight, maxCross)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArraySum(nums, 0, len(nums) - 1)
        