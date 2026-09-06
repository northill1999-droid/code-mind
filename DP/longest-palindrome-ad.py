# https://leetcode.cn/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):  # dp[i+1][j-1] 去掉两端字符后的内部子串
                    dp[i][j] = True

                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start: start +  max_len]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))