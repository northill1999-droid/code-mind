# https://leetcode.cn/problems/combination-sum-ii/description/?envType=problem-list-v2&envId=array

from typing import List
import collections

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(idx: int, rest: int):
            nonlocal combine

            if rest == 0:
                ans.append(combine[:])
                return

            if idx == len(freq) or rest < freq[idx][0]:
                return


            dfs(idx + 1, rest)


            most = min(rest // freq[idx][0], freq[idx][1])
            for i in range(1, most + 1):

                combine.append(freq[idx][0])
                dfs(idx + 1, rest - i * freq[idx][0])

            combine = combine[:-most]


        freq = sorted(collections.Counter(candidates).items())

        ans = []
        combine = []

        dfs(0, target)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))  
    # [[1,1,6], [1,2,5], [1,7], [2,6]]