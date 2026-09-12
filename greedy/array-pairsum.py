# https://leetcode.cn/problems/array-partition/
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        final = 0
        for i in nums[-2::-2]:
            final += i
        return final


if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayPairSum([6,2,6,5,1,2]))