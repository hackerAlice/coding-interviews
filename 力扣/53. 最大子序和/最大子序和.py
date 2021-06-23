#!/usr/bin/python

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 表示以第i个数结尾的最大子序列和

        if len(nums) < 2:
            return nums[0]

        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + dp[i-1] > nums[i]:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
        return max(dp)
