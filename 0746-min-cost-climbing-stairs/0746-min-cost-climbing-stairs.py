class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        for i in range(len(cost)-3,-1,-1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0],cost[1])


        """
        length = len(cost)
        def minCost(step):
            if step < 0 or step >= length:
                return 0
            elif length-2  <= step < length:
                return cost[step]
            return cost[step] + min(minCost(step+1), minCost(step+2))

        return min(minCost(0), minCost(1))
        """