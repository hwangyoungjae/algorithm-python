from .solution2 import Solution
from .treenode import TreeNode


class Test:
    def test_case1(self):
        solution = Solution()
        root = TreeNode.from_array([1, 2, 2, 3, 4, 4, 3])
        assert solution.isSymmetric(root) is True

    def test_case2(self):
        solution = Solution()
        root = TreeNode.from_array([1, 2, 2, None, 3, None, 3])
        assert solution.isSymmetric(root) is False

    def test_case3(self):
        solution = Solution()
        root = TreeNode.from_array([1, 2, 2, 3, 4, 4, 3, 11, 12, 13, 14, 14, 13, 12, 11])
        assert solution.isSymmetric(root) is True
