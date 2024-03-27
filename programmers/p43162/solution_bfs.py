import logging
from collections import deque

logger = logging.getLogger('P43162')


def bfs(n, computers, visited, start):
    visited[start] = 1

    dq = deque()
    dq.append(start)

    while dq:
        i = dq.popleft()
        for j in range(n):
            if computers[i][j] and not visited[j]:
                visited[j] = 1
                dq.append(j)


def solution(n, computers) -> int:
    answer = 0
    visited = [0 for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, visited, i)
            answer += 1

    return answer
