# https://leetcode.cn/problems/next-permutation/description/?envType=problem-list-v2&envId=array

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List:
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # 破坏升序 -> 右侧必然存在比之更大的数字
            while j >= 0 and nums[j] <= nums[i]:  # find the first bigger one than nums[i] 
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))  # [1,3,2]
    print(sol.nextPermutation([1,1,5]))  # [1,5,1]
    print(sol.nextPermutation([3,2,1]))  # [1,2,3]
    print(sol.nextPermutation([1,3,2]))  # [2,1,3]
