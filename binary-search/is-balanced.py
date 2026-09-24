# https://leetcode.cn/problems/balanced-binary-tree/solutions/377216/ping-heng-er-cha-shu-by-leetcode-solution/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(root: TreeNode | None) -> int:
            if not root:
                return 0

            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    