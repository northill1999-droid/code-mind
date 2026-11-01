# https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/solutions/1054870/zui-xiao-cao-zuo-ci-shu-shi-shu-zu-yuan-3meg3/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        for num in nums:
            res += num - min_num
        return res


