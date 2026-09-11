class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):  # f(n) = f(n-1) + f(n-2)
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    