#!/usr/bin/python3

"""
暴力破解发：会超时
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profile = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profile:
                    max_profile = prices[j] - prices[i]

        return max_profile