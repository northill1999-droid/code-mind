# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
                
            fast += 1

        return slow

if __name__ == "__main__":
    sol = Solution()
    result = sol.removeDuplicates([1,1,2])
    print(result)