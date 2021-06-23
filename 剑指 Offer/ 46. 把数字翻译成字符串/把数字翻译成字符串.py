#!/usr/bin/python3

import string


class Solution:
    def translateNum(self, num: int) -> int:
        d = dict(zip(list(range(26)), string.ascii_lowercase))

        num_str = str(num)

        dp = [0] * (len(num_str)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(num_str)):
            if '10' <= num_str[i-1:i+1] <= '25':
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[len(num_str)]