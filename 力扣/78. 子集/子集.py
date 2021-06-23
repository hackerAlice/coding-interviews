#!/usr/bin/python3

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, tmp):
            res.append(tmp)
            for i in range(index, n):
                backtrack(i + 1, tmp + [nums[i]])

        n = len(nums)
        res = []
        backtrack(0, [])
        return res
