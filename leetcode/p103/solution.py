from collections import deque
from typing import List, Optional

from leetcode.p103.treenode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq: deque[TreeNode] = deque()
        if root is not None:
            dq.append(root)

        result = []
        lv = 1
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()

                if lv % 2 == 0:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)

                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            result.append(level)
            lv += 1
        return result
