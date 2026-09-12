# https://leetcode.cn/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = n - 1
            target = -nums[i]
            
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue

                while j < k and nums[j] + nums[k] > target:
                    k -= 1

                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([0,0,0]))