# https://leetcode.cn/problems/contains-duplicate-ii/
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, value in enumerate(nums):
            if value in pos and i - pos[value] <= k:
                return True
            pos[value] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))