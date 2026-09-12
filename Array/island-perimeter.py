# https://leetcode.cn/problems/island-perimeter/
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0

            grid[x][y] = 2
            res = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                res += dfs(tx, ty)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
                    # print("HI")

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
    # print(sol.islandPerimeter([[1]]))  # 4
    # print(sol.islandPerimeter([[1,0]]))  # 4
