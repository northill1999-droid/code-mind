# 链接：https://leetcode.cn/problems/climbing-stairs-ii/solutions/4050907/pa-lou-ti-ii-by-leetcode-solution-7kcl/

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0
        for i in range(n):
            a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]
        return c


