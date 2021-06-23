#!/usr/bin/python3

from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        path, ans = list(), list()
        length = len(S)

        def backstrack(s: str):
            if len(path) == length:
                ans.append("".join(path))
                return

            for i in range(len(s)):
                path.append(s[i])
                backstrack(s[:i] + s[i + 1:])
                path.pop()

        backstrack(S)
        return ans
