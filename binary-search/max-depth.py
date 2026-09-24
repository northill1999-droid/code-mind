# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)

            return max(left_height, right_height) + 1
        