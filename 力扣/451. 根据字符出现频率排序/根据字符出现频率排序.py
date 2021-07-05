#!/usr/bin/python

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return

        c = collections.Counter(s)
        c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        # print(c)
        return ''.join([item[0] * item[1] for item in c])
