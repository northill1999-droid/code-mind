# https://leetcode.cn/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numsRows: int) -> List[List[int]]:
        triangles = []
        for i in range(numsRows+1):
            lst = [1] * (i + 1)
            for j in range(1, i):
                lst[j] = triangles[i-1][j-1] + triangles[i-1][j]

            triangles.append(lst)

        # return triangles
        return triangles[numsRows]

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(3))
