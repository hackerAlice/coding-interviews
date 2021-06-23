#!/usr/bin/python3

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        res = set()
        for c in s:
            if c not in res:
                res.add(c)
            else:
                res.remove(c)

        return len(res)<=1