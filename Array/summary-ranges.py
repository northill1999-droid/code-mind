# https://leetcode.cn/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst = []
        lst1 = []
        for i in range(len(nums)):
            lst1.append(nums[i])
            if i >= len(nums)-1:
                lst.append(lst1)
                break

            if nums[i] != nums[i+1]-1:
                lst.append(lst1)
                lst1 = []
                continue

        lst2 = []
        for i in lst:
            if len(i) >= 2:
                lst2.append(f"{i[0]}->{i[-1]}")
                continue
            lst2.append(f"{i[0]}")

        return lst2


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,2,3,4,6,8,9]))