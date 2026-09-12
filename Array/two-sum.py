# https://leetcode.cn/problems/two-sum/
class Solution:
    def towSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        ind = 0
        for i in nums:
            if (target-i) in lst:
                return [lst.index(target-i), ind]
            lst.append(i)
            ind += 1

        return False

if __name__ == "__main__":
    apple = Solution()
    banana = apple.towSum([2, 7, 11, 15], 9)
    banana2 = apple.towSum([3, 2, 4], 6)
    print(banana)
    print(banana2)