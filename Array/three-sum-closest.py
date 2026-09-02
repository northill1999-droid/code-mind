from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    lst.append((nums[i] + nums[j] + nums[k]) - target)

        ans = lst[0]
        # ind = 0
        for i in range(len(lst)):
            if abs(lst[i]) < abs(ans):
                ans = lst[i]

        return ans + target


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))  # 2
    print(sol.threeSumClosest([0,0,0], 1))  # 0
