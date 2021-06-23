#!/usr/bin/python3
"""
使用动态规划
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1]+nums[i]

        return max(dp)
