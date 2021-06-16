#!/usr/bin/python3


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        number = list(range(n))
        cur = 0
        while len(number) != 1:
            next = (cur + m + len(number) - 1) % len(number)
            number.pop(next)
            if next == len(number):
                cur = 0
            else:
                cur = next
        return number[0]
