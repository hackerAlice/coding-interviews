#!/usr/bin/python3

from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
        visited = [[0] * n for _ in range(m)]

        def dfs(i, j):
            nonlocal temp
            nonlocal visited
            if land[i][j]:
                return

            temp += 1

            for di, dj in directions:
                x = i + di
                y = j + dj

                if 0 <= x < m and 0 <= y < n and not land[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    dfs(x, y)

        ans = []
        for i in range(m):
            for j in range(n):
                if not land[i][j] and not visited[i][j]:
                    visited[i][j] = 1
                    temp = 0
                    dfs(i, j)
                    ans.append(temp)

        return sorted(ans)


if __name__ == "__main__":
    print(Solution().pondSizes([[0, 2, 1, 0], [0 , 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
