#!/usr/bin/python3

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = list()
        for index in range(len(mat)):
            d.append((index, mat[index].count(1)))

        d.sort(key=lambda x: (x[1], x[0]))

        print(d)

        return [item[0] for item in d[:k]]