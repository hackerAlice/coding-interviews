#!/usr/bin/python3

class Solution:
    def waysToStep(self, n: int) -> int:

        if n < 3:
            return n

        if n == 3:
            return 4

        a, b, c = 1, 2, 4

        for i in range(4, n + 1):
            a, b, c = b, c, (a + b + c) % 1000000007
        return c