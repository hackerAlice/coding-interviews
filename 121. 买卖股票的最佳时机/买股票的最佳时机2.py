#!/usr/bin/python3

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profile = 0
        min_price = float('infinity')

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profile:
                max_profile = prices[i] - min_price

        return max_profile