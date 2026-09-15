# https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/?envType=daily-question&envId=2026-09-15

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right] and (length <= 2 or is_palindrome[left+1][right-1]):
                    is_palindrome[left][right] = True

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if is_palindrome[j][i-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPalindromes("abaccdbbd", 3))  # 2
    print(sol.maxPalindromes("adbcda", 2))  # 0
