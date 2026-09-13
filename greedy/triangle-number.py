# https://leetcode.cn/problems/valid-triangle-number/description/

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def check(a, b, c):
            if a + b > c and a + c > b and b + c > a:
                return True
            return False

        ans = 0

        slow = 0
        mid = 1
        fast = 2
        while slow < len(nums) - 2:
            if check(nums[slow], nums[mid], nums[fast]):
                ans += 1

            fast += 1
            if fast == len(nums):
                mid += 1
                fast = mid + 1
                if mid == len(nums) - 1:
                    slow += 1
                    mid = slow + 1
                    fast = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.triangleNumber([4,2,3,4]))  # 4
    print(sol.triangleNumber([2,2,3,4]))  # 3
    