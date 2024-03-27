from .solution import solution


class Test:
    def test_case1(self):
        assert solution([3, 1, 2, 3]) == 2

    def test_case2(self):
        assert solution([3, 3, 3, 2, 2, 4]) == 3

    def test_case3(self):
        assert solution([3, 3, 3, 2, 2, 2]) == 2
