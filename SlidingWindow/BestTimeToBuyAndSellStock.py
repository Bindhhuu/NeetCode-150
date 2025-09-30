class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minn = float('inf')
        max_profit = 0

        for i in prices:
            if i < minn:
                minn = i

            profit = i - minn

            if profit > max_profit:
                max_profit = profit

        return max_profit
