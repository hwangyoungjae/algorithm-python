from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    maxX = max([max(o[0], o[2]) for o in rectangle])
    maxY = max([max(o[1], o[3]) for o in rectangle])

    maps = [[0] * (maxX * 2 + 2) for _ in range(maxY * 2 + 2)]

    for pos in rectangle:
        lbx, lby = pos[0] * 2, pos[1] * 2
        rtx, rty = pos[2] * 2, pos[3] * 2

        for x in range(lbx, rtx + 1):
            for y in range(lby, rty + 1):
                maps[y][x] = 1

    for pos in rectangle:
        lbx, lby = pos[0] * 2, pos[1] * 2
        rtx, rty = pos[2] * 2, pos[3] * 2

        for x in range(lbx + 1, rtx):
            for y in range(lby + 1, rty):
                maps[y][x] = 0

    dq = deque()
    dq.append((characterX * 2, characterY * 2))

    while dq:
        x, y = dq.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return (maps[y][x] - 1) // 2
        for dx, dy in [(0, +1), (0, -1), (+1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if not (nx == characterX * 2 and ny == characterY * 2) and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                dq.append((nx, ny))

    return 0
