class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[amount+1] * (amount+1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[amount] if dp[amount]!=(amount+1) else -1 

        """
        res = amount+1
        stack = [(amount, 0)]

        while stack:
            x, nb = stack.pop()
            if x == 0 and nb < res:
                res = nb
            for coin in coins :
                if x - coin >= 0:
                    stack.append((x-coin, nb+1))

        return res if res != amount + 1 else -1
        """