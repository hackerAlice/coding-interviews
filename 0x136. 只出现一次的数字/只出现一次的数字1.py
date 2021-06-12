#!/usr/bin/python3

"""
使用异或
"""

from typing import  List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

