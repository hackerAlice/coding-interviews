#!/usr/bin/python3

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        d = list(enumerate(costs))
        d.sort(key=lambda x: x[1])
        ans = 0

        for index, value in d:
            if coins - value >= 0:
                ans += 1
                coins -= value
            else:
                break

        return ans
