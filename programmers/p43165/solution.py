from __future__ import annotations

from collections import deque
from typing import List


def bfs(numbers: List[int], target: int) -> int:
    N = len(numbers)

    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    answer = 0
    while q:
        n, idx = q.popleft()

        if idx + 1 >= N:
            if n == target:
                answer += 1
            continue
        q.append((n + numbers[idx + 1], idx + 1))
        q.append((n - numbers[idx + 1], idx + 1))

    return answer


def dfs(numbers: List[int], target: int) -> int:
    N = len(numbers)

    def search(n: int, idx: int) -> int:
        if idx + 1 >= N:
            if n == target:
                return 1
            return 0
        return search(n + numbers[idx + 1], idx + 1) + search(n - numbers[idx + 1], idx + 1)

    return search(numbers[0], 0) + search(-numbers[0], 0)


def solution(numbers: List[int], target: int) -> int:
    return dfs(numbers, target)
