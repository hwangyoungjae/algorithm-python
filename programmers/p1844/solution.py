from __future__ import annotations

from collections import deque
from typing import List

DIRECTIONS = {
    'N': (+1, 0),  # 동
    'S': (-1, 0),  # 서
    'E': (0, +1),  # 남
    'W': (0, -1),  # 북
}


def solution(maps: List[List[int]]) -> int:
    xSize = len(maps[0])
    ySize = len(maps)

    visit = [[0 for _ in range(xSize)] for _ in range(ySize)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1

    while q:
        x, y = q.popleft()
        for direction in ('N', 'S', 'E', 'W'):
            dx = DIRECTIONS[direction][0]
            dy = DIRECTIONS[direction][1]
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= xSize or ny < 0 or ny >= ySize:
                continue
            # if 0 <= nx < xSize and 0 <= ny < ySize:
            if maps[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append((nx, ny))
                visit[ny][nx] = visit[y][x] + 1
    if visit[ySize - 1][xSize - 1] == 0:
        return -1
    return visit[ySize - 1][xSize - 1]
