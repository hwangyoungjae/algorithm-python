from collections import deque


def compare(s1, s2):
    equal = 0
    idx = 0
    for c in s1:
        if c == s2[idx]:
            equal += 1
        idx += 1
    return equal


def bfs(begin, target, words):
    wordLength = len(begin)
    if not (target in words):
        return 0

    check = {k: 0 for k in words}
    dq = deque()

    check[begin] = 0
    dq.append(begin)

    while dq:
        s = dq.popleft()

        for word in words:
            c = compare(s, word)

            if check[word] == 0 and c == (wordLength - 1):
                check[word] = check[s] + 1
                dq.append(word)

    return check[target]


def solution(begin, target, words):
    return bfs(begin, target, words)
