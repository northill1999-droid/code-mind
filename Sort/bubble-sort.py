from typing import List

class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        
        while True:
            found = 0
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    found = 1

            if found == 0:
                return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.bubbleSort([3, -5, 0, 12, -8, 7, 3, 15, -2, 6, 6, 0, -4, 9, 11, -1, 14, 2, -7, 5]))
    print(sol.bubbleSort([64, 34, 25, 12, 22, 11, 90]))
