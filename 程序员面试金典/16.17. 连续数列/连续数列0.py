#!/usr/bin/python3

"""
使用动态规划解决
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [-float('infinity')] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
