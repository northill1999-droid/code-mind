# https://leetcode.cn/problems/intersection-of-two-arrays-ii/
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        tag = []
        for i in nums2 if len(nums2) < len(nums1) else nums1:
            for index, j in enumerate(nums1 if len(nums1) > len(nums2) else nums2):
                if i == j and (index not in tag):
                    lst.append(i)
                    tag.append(index)
                    break

        return lst
        
if __name__ == "__main__":
    sol = Solution()
    # print(sol.intersect([1,2,2,1], [2,2]))
    # print(sol.intersect([1,2,2,1], [2]))
    # print(sol.intersect([1,2], [1,1]))
    print(sol.intersect([3,1,2], [1,1]))