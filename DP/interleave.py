# https://leetcode.cn/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        if n + m != t:
            return False
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] |= dp[i-1][j] and s1[i-1] == s3[p]
                if j > 0:
                    dp[i][j] |= dp[i][j-1] and s2[j-1] == s3[p]
        
        return dp[n][m]
