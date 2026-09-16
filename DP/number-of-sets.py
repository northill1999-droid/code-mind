# https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/?envType=daily-question&envId=2026-09-16

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        
        dp = [1] * n
        prefix_sums = [0] * (n + 1)

        for j in range(n):
            prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % mod

        for _ in range(k):

            dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix_sums[j]) % mod

            for j in range(n):
                prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % mod

        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSets(4, 2))  # 5
    print(sol.numberOfSets(3, 1))  # 3

