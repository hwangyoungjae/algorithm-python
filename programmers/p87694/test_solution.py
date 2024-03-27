from .solution import solution


class Test:
    def test_example1(self):
        assert solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8) == 17

    def test_example2(self):
        assert solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1) == 11

    def test_example3(self):
        assert solution([[1, 1, 5, 7]], 1, 1, 4, 7) == 9

    def test_example4(self):
        assert solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10) == 15

    def test_example5(self):
        assert solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3) == 10
