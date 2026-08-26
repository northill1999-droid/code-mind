from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)

        while i < n:
            low = i
            i += 1

            while i < n and nums[i-1] == nums[i] - 1:
                i += 1

            high = i - 1
            
            if low < high:
                res.append(f"{nums[low]}->{nums[high]}")
                continue
            res.append(f"{nums[low]}")
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))