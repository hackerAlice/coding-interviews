#!/usr/bin/python3

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        a = [[0 for _ in range(8)] for _ in range(8)]
        for r, c in queens:  # 状态标记  queen所在的位置 置1
            a[r][c] = 1

        res = []
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]  # 8个方向
        for dr, dc in dirs:  # 遍历 每次照着一个方向一路查找
            r, c = king[0], king[1]
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:  # 只要还没出边界
                if a[nr][nc] == 1:
                    res.append([nr, nc])
                    break
                nr = nr + dr  # 按照这个方向一直找  直到找到或者和出了范围
                nc = nc + dc

        return res