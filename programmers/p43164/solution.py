import collections
from typing import List, Dict


def dfs(tickets: List[List[str]]) -> List[str]:
    ticketMap: Dict[str, List[str]] = collections.defaultdict(list)
    for src, dst in tickets:
        ticketMap[src].append(dst)
    [q.sort() for q in ticketMap.values()]

    path = []

    def search(ticket: str):
        while ticketMap[ticket]:
            search(ticketMap[ticket].pop(0))
        path.append(ticket)

    search('ICN')
    return path[::-1]


def solution(tickets: List[List[str]]) -> List[str]:
    return dfs(tickets)
