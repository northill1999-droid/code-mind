# https://leetcode.cn/problems/binary-tree-preorder-traversal/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._preorder(root, res)
        return res

    def _preorder(self, node: Optional[TreeNode], res: List[int]):
        if node is None:
            return

        res.append(node.val)
        self._preorder(node.left, res)
        self._preorder(node.right, res)
