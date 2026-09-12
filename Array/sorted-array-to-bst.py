# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return f"TreeNode({self.val}, left={self.left}, right={self.right})"

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        root = helper(0, len(nums) - 1)
        return root

        # def level_order(root: Optional[TreeNode]) -> List:
        #     if not root:
        #         return []
            
        #     result = []
        #     queue = [root]
            
        #     while queue:
        #         node = queue.pop(0)
        #         if node:
        #             result.append(node.val)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #         else:
        #             result.append(None)
            
        #     while result and result[-1] is None:
        #         result.pop()
            
        #     return result

        # return level_order(root)

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9]))