#!/usr/bin/python3

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = list()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    zeros.append((i, j))

        for i, j in zeros:
            for col in range(n):
                matrix[i][col] = 0

            for row in range(m):
                matrix[row][j] = 0