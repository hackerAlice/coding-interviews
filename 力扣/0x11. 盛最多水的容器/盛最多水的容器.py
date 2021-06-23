#!/usr/bin/python

"""
双指针法
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        low, high = 0, len(height)-1
        ans = 0

        while low < high:
            area = min(height[low], height[high]) * (high-low)
            ans = max(ans, area)

            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1

        return ans