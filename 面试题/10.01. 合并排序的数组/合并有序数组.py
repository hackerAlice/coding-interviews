#!/usr/bin/python3

from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()