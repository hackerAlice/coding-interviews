#!/usr/bin/python3

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:

        path = []
        result = set()
        length = len(s)

        def backstrack(s: str):
            if len(path) == length:
                result.add(''.join(list(path)))
                return
            for i in range(len(s)):
                path.append(s[i])
                backstrack(s[:i] + s[i + 1:])
                path.pop()

        if not s:
            return []

        backstrack(s)
        return list(result)


