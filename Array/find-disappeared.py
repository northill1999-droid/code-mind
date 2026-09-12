# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # lst = []
        # for i in range(1, len(nums)+1):
        #     if i not in nums:
        #         lst.append(i)

        # return lst

        n = len(nums)
        lst = list(range(1, n+1))
        for i in nums:
            lst[i - 1] += n

        lst1 = []
        for i in range(len(nums)):
            if lst[i] <= n:
                lst1.append(i + 1)
        return lst1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([1,1]))
