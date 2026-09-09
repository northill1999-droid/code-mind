# https://leetcode.cn/problems/combination-sum/?envType=problem-list-v2&envId=array

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combine = []

        def dfs(idx: int, target: int):

            if idx == len(candidates):
                return
            if target == 0:
                ans.append(combine.copy())
                return


            dfs(idx + 1, target)


            if target - candidates[idx] >= 0:

                combine.append(candidates[idx])

                dfs(idx, target - candidates[idx])

                combine.pop()

        dfs(0, target)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
