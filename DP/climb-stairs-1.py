# https://leetcode.cn/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # if n <= 2:
        #     return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# f(n) = f(n-1) + f(n-2)
