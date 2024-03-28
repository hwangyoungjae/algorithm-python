from .solution import Solution
from .treenode import TreeNode


class Test:
    def test_case1(self):
        root = TreeNode.from_array([3, 9, 20, None, None, 15, 7])
        assert Solution().zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

    def test_case2(self):
        root = TreeNode.from_array([1])
        assert Solution().zigzagLevelOrder(root) == [[1]]

    def test_case3(self):
        root = TreeNode.from_array([])
        assert Solution().zigzagLevelOrder(root) == []
