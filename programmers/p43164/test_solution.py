from .solution import solution


class Test:
    def test_example1(self):
        tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
        expected = ["ICN", "JFK", "HND", "IAD"]
        assert solution(tickets) == expected

    def test_example2(self):
        tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
        expected = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
        assert solution(tickets) == expected

    def test_example3(self):
        tickets = [["ICN", "SFO"], ["SFO", "JFK"], ["JFK", "SFO"], ["SFO", "ATL"]]
        expected = ['ICN', 'SFO', 'JFK', 'SFO', 'ATL']
        assert solution(tickets) == expected
