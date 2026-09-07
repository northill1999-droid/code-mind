# https://leetcode.cn/problems/max-consecutive-ones/submissions/747566769/?envType=problem-list-v2&envId=array

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                # print(count, end=' ')

                if count > ans:
                    ans = count

                continue
            
            print()
            count = 0

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    