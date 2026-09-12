# https://leetcode.cn/problems/majority-element/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 0
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        if count > len(nums) / 2:
            return 0
        
        ind = 0
        while sum(nums) != 0:
            count = 0
            num = nums[ind]
            for i in range(len(nums)):
                if nums[i] == num:
                    count += 1
                    nums[i] = 0

                if count > len(nums) / 2:
                    return num
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    break
                ind += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([6,5,5]))
                