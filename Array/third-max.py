# https://leetcode.cn/problems/third-maximum-number/
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = sorted(list(set(nums)))
        if len(lst) < 3:
            return max(lst)
        return lst[-3]

if __name__ == "__main__":
    sol = Solution()
    print(sol.thirdMax([2, 2, 3, 1]))
        