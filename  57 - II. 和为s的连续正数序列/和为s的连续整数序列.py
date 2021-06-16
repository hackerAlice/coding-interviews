#!/usr/bin/python3

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        left, right, s, res = 1, 2, 3, list()

        while left < right:
            if target == s:
                res.append(list(range(left, right + 1)))

            if s >= target:
                s -= left
                left += 1
            else:
                right += 1
                s += right

        return res