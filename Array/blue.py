# https://leetcode.cn/problems/count-servers-that-communicate/solutions/101819/tong-ji-can-yu-tong-xin-de-fu-wu-qi-by-leetcode-so/

from collections import Counter
from typing import List
from typing_extensions import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        
        return ans


