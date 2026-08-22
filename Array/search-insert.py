class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0
        for i in nums:
            if i >= target:
                return ind
            ind += 1
            if ind >= len(nums):
                return ind


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))

    print(sol.searchInsert([1, 3, 5, 6], 2))

    print(sol.searchInsert([1, 3, 5, 6], 7))