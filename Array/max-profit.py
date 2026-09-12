# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > profit:
                profit = i - min_price

        return profit

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))