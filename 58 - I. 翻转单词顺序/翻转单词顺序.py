#!/usr/bin/python3


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s

        return ' '.join(s.strip().split()[::-1])
