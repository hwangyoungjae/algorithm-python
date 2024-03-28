# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, Sequence

from leetcode.p101.treenode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root)

        for v1, v2 in zip(self.search_left(root), self.search_right(root)):
            if v1 != v2:
                return False
        return True

    def search_left(self, root: TreeNode) -> Sequence[int]:
        q = deque()
        q.append(root.left)
        while q:
            node = q.popleft()
            if node is None:
                yield None
            else:
                yield node.val
                q.append(node.left)
                q.append(node.right)

    def search_right(self, root: TreeNode) -> Sequence[int]:
        q = deque()
        q.append(root.right)
        while q:
            node = q.popleft()
            if node is None:
                yield None
            else:
                yield node.val
                q.append(node.right)
                q.append(node.left)
