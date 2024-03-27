from .solution_bfs import solution


class Test:
    def test_example1(self):
        print()
        n = 3
        computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        expected = 2
        assert solution(n, computers) == expected

    def test_example2(self):
        print()
        n = 3
        computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
        expected = 1
        assert solution(n, computers) == expected

    def test_example3(self):
        # print()
        n = 6
        computers = [
            [1, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 0, 1],
        ]
        expected = 3
        assert solution(n, computers) == expected
