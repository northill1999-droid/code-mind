# https://leetcode.cn/problems/majority-element/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for key, value in d.items():
            if value > len(nums)/2:
                return key


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([6,5,5]))
    