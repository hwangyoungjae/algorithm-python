from .treenode import TreeNode


class Test:
    def test_from_array_case1(self):
        node = TreeNode.from_array([1, 2, 2, 3, 4, 4, 3])
        assert node.val == 1
        assert node.left.val == 2
        assert node.right.val == 2
        assert node.left.left.val == 3
        assert node.left.right.val == 4
        assert node.right.left.val == 4
        assert node.right.right.val == 3

    def test_from_array_case2(self):
        node = TreeNode.from_array([1, 2, 2, None, 3, None, 3])
        assert node.val == 1
        assert node.left.val == 2
        assert node.right.val == 2
        assert node.left.left is None
        assert node.left.right.val == 3
        assert node.right.left is None
        assert node.right.right.val == 3
