import logging

logger = logging.getLogger('P43162')


def dfs(i, computers, visited):
    for j, v in enumerate(computers[i]):
        if not visited[j] and v == 1:
            visited[j] = 1
            dfs(j, computers, visited)


def solution(n, computers) -> int:
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, computers, visited)
            answer += 1

    return answer
