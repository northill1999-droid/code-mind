# https://leetcode.cn/problems/permutations/solutions/218275/quan-pai-lie-by-leetcode-solution-2/?envType=problem-list-v2&envId=array

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first + 1)
                
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res

