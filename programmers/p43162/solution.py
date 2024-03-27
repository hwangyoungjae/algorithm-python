from typing import List, Tuple, Union


def find1(n: int, computers: List[List[int]]) -> Union[Tuple[int, int], None]:
    for i in range(n):
        for j in range(i, n):
            if computers[i][j] == 1:
                return i, j
    return None


def solution(n: int, computers: List[List[int]]) -> int:
    answer = 0
    while 1:
        founded = find1(n, computers)
        if founded is None:
            return answer
        i, j = founded

        def dfs(i: int):
            for j, v in enumerate(computers[i]):
                print((i, j), v)
                if v == 1:
                    computers[i][j] = 0
                    computers[j][i] = 0
                    dfs(j)

        dfs(i)
        for row in computers:
            print(row)
        answer += 1
