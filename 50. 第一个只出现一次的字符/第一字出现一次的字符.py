#!/usr/bin/python3


class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        d = dict()

        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        for k, v in d.items():
            if v == 1:
                return k

        return " "