# https://leetcode.cn/problems/valid-triangle-number/description/

from typing import List

class Solution:  # 排序 + 双指针
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        ans = 0
        for fast in range(n - 1, 1, -1):
            left, right = 0, fast - 1
            while left < right:
                if nums[left] + nums[right] > nums[fast]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.triangleNumber([4,2,3,4]))  # 4
    print(sol.triangleNumber([2,2,3,4]))  # 3
    