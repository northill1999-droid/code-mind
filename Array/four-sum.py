from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # ans = [[]
        nums.sort()

        lst = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, len(nums) - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        lst.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif curr_sum > target:
                        right -= 1

                    else:
                        left += 1
                    
        return lst


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))  # [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
    print(sol.fourSum([2,2,2,2,2], 8))  # [[2,2,2,2]]
