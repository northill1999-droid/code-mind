class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0, 1, 0, 3, 12]))

    print(sol.moveZeroes([4,2,4,3,0,5,1,0,0,0]))

    # print(sol.moveZeroes([0, 0, 1]))

    # print(sol.moveZeroes([-1, 2, 3]))

    # print(sol.moveZeroes([0]))


