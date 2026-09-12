# https://leetcode.cn/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1

        return ind

if __name__ == "__main__":
    sol = Solution()     
    result = sol.removeElement([0,1,2,2,3,0,4,2], 2)
    print(result)