from typing import List

class Solution:
    def selectSort(self, nums: List[int]) -> List[int]:
        # right = len(nums) - 1
        for left in range(len(nums)-1):
            min_index = left

            for i in range(left, len(nums)):
                if nums[min_index] > nums[i]:
                    min_index = i
            
            nums[left], nums[min_index] = nums[min_index], nums[left]

        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.selectSort([3, -5, 0, 12, -8, 7, 3, 15, -2, 6, 6, 0, -4, 9, 11, -1, 14, 2, -7, 5]))
    print(sol.selectSort([64, 34, 25, 12, 22, 11, 90]))
    