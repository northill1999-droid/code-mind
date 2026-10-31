# https://leetcode.cn/problems/twisted-mirror-path-count/solutions/4043260/tong-ji-jing-zi-fan-she-lu-jing-shu-mu-b-fg88/

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # f[i][j][0]：通过向下移动进入 (i, j)
        # f[i][j][1]：通过向右移动进入 (i, j)
        f = [[[0, 0] for _ in range(n)] for _ in range(m)]
        f[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[i][j][0] = f[i - 1][j][0] + f[i - 1][j][1]
                    else:
                        f[i][j][0] = f[i - 1][j][1]
                    f[i][j][0] %= MOD

                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[i][j][1] = f[i][j - 1][0] + f[i][j - 1][1]
                    else:
                        f[i][j][1] = f[i][j - 1][0]
                    f[i][j][1] %= MOD

        return (f[m - 1][n - 1][0] + f[m - 1][n - 1][1]) % MOD


