from .solution import solution


class Test:
    def test_example1(self):
        assert solution([1, 1, 1, 1, 1], 3) == 5

    def test_example2(self):
        assert solution([4, 1, 2, 1], 4) == 2
