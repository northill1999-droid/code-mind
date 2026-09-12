# https://leetcode.cn/problems/intersection-of-two-arrays/
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            if i in lst:
                continue
            for j in nums2:
                if i == j:
                    lst.append(i)
                    break

        return lst

if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))
    print(sol.intersection([4,9,5], [9,4,9,8,4]))
        