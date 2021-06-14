#!/usr/bin/python3

from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr: return
        arr = sorted(arr)
        if k > len(arr):
            return arr
        else:
            return arr[:k]