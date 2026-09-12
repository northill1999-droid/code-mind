# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        ind_left = self.search_left(nums, target)

        ind_right = ind_left

        if ind_left != -1:
            ind_right = self.search_right(nums, target)

        return [ind_left, ind_right]

    # @staticmethod
    def search_left(self, nums, target) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:  # nums[mid] > target
                right = mid - 1

        if nums[left] != target:
            return -1
        
        return left

    def search_right(self, nums, target) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right + 1) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid
                # print(f"left: {left}, right: {right}")
            else:  # nums[mid] < target
                right = mid - 1
        
        return left
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))  # [3, 4]
    print(sol.searchRange([5,7,7,8,8,10], 6))  # [-1, -1]
    print(sol.searchRange([], 0))  # [-1, -1]
