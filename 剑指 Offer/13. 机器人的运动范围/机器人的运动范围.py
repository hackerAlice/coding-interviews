#!/usr/bin/python3


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i // 10 + i % 10 + j // 10 + j % 10 <= k:
                    visited[i][j] = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                return 0
            visited[x][y] = 1
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)