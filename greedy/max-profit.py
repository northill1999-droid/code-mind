# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/?envType=problem-list-v2&envId=greedy 

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans

    