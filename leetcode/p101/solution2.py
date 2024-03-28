from typing import Optional

from leetcode.p101.treenode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        return (left.val == right.val
                and self.isMirror(left.left, right.right)
                and self.isMirror(left.right, right.left))
