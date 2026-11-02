# https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/solutions/1501230/zui-shao-yi-dong-ci-shu-shi-shu-zu-yuan-xt3r2/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)


