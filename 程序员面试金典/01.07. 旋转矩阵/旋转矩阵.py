#!/usr/bin/python3

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        n = len(matrix)

        temp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                temp[j][n-1-i] = matrix[i][j]

        matrix[:] = temp
