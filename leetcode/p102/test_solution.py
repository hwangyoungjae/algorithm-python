from .solution2 import Solution
from .treenode import TreeNode


class Test:
    def test_case1(self):
        root = TreeNode.from_array([3, 9, 20, None, None, 15, 7])
        assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

    def test_case2(self):
        root = TreeNode.from_array([1])
        assert Solution().levelOrder(root) == [[1]]

    def test_case3(self):
        root = TreeNode.from_array([])
        assert Solution().levelOrder(root) == []

    def test_case4(self):
        root = TreeNode.from_array([1, 2])
        assert Solution().levelOrder(root) == [[1], [2]]

    def test_case5(self):
        root = TreeNode.from_array([1, 2, 3, 4, None, None, 5])
        assert Solution().levelOrder(root) == [[1], [2, 3], [4, 5]]
