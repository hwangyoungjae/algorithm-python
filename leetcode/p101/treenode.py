from __future__ import annotations

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_array(cls, array: List[int]) -> TreeNode:
        nodes: List[TreeNode | None] = [None for _ in array]
        for i, val in enumerate(array, 1):
            nodeIdx = i - 1
            parentIdx = i // 2 - 1
            if i == 1:
                nodes[i - 1] = TreeNode(val)
            else:
                if val is not None:
                    nodes[nodeIdx] = TreeNode(val)
                    if i % 2:
                        nodes[parentIdx].right = nodes[nodeIdx]
                    else:
                        nodes[parentIdx].left = nodes[nodeIdx]

        return nodes[0]

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"val={self.val},"
                f"left={None if self.left is None else self.left.val},"
                f"right={None if self.right is None else self.right.val})")
