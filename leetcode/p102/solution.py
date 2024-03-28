from typing import Optional, List

from leetcode.p102.treenode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.search(1, root, result)
        return result

    def search(self, level: int, node: TreeNode, result: List[List[int]]):
        if node is None:
            return
        try:
            result[level - 1].append(node.val)
        except IndexError:
            result.append([node.val])
        self.search(level + 1, node.left, result)
        self.search(level + 1, node.right, result)
