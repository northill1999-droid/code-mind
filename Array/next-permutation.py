# https://leetcode.cn/problems/next-permutation/description/?envType=problem-list-v2&envId=array

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List:
        # to be continue

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))  # [1,3,2]
    print(sol.nextPermutation([1,1,5]))  # [1,5,1]
    print(sol.nextPermutation([3,2,1]))  # [1,2,3]
    print(sol.nextPermutation([1,3,2]))  # [2,1,3]
