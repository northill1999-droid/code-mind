# https://leetcode.cn/problems/rectangle-overlap/?envType=daily-question&envId=2026-09-14

from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2]:
            return False
        if rec1[3] < rec2[1] or rec1[1] > rec2[3]:
            return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isRectangleOverlap([0,0,2,2], [1,1,3,3]))  # true
    # print(sol.isRectangleOverlap([0,0,1,1], [1,0,2,1]))  # false
    # print(sol.isRectangleOverlap([0,0,1,1], [2,2,3,3]))  # false
    print(sol.isRectangleOverlap([5,15,8,18], [0,3,7,9]))  # false

