from collections import deque
from typing import Optional, List

from leetcode.p102.treenode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq: deque[TreeNode] = deque()
        if root is not None:
            dq.append(root)

        result = []
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            result.append(level)
        return result
