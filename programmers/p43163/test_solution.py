from .solution import compare, solution


class Test:
    def test_compare(self):
        assert compare("AAA", "AAA") == 3
        assert compare("AAA", "AAB") == 2
        assert compare("AAA", "ABC") == 1
        assert compare("AAA", "BCD") == 0

    def test_example1(self):
        assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]) == 4

    def test_example2(self):
        assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]) == 0

    def test_example3(self):
        assert solution('aaaa', 'cccc', ["aaac", "aacc", "accc", "cccc"]) == 4
