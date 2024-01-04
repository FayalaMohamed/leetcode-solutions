class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = [False] * (24 * 60)
        for time in timePoints:
            t = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
            if minutes[t]:  # time point already exists
                return 0
            minutes[t] = True

        prev = next = None
        min_difference = float('inf')
        for i in range(24 * 60):
            if minutes[i]:
                if prev is not None:
                    min_difference = min(min_difference, i - prev)
                else:
                    next = i
                prev = i

        min_difference = min(min_difference, next + 24 * 60 - prev)

        return min_difference
        