# https://leetcode.cn/problems/find-target-indices-after-sorting-array/solutions/1127136/zhao-chu-shu-zu-pai-xu-hou-de-mu-biao-xi-2o22/?envType=daily-question&envId=2026-10-19

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] == target:
                res.append(i)
        return res

