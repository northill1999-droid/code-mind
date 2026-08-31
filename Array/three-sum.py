class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # print(nums)

        ans = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:

                for j in range(i+1, len(nums)):
                    if j == i+1 or nums[j] != nums[j - 1]:

                        for k in list(range(j+1, len(nums)))[::-1]:
                            if k == len(nums) - 1 or nums[k] != nums[k + 1]:

                                if nums[i] + nums[j] + nums[k] == 0:
                                    ans.append([nums[i], nums[j], nums[k]])


        # ans1 = []
        # for i in range(len(ans)):
        #      lst1 = sorted(ans[i])
        #      if lst1 in ans1:
        #          continue
        #      ans1.append(lst1)
                     
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([0,0,0]))