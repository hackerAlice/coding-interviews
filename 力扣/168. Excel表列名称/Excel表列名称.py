#!/usr/bin/python3

import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        strs = string.ascii_uppercase
        # strs = strs[-1] + strs[:-1]
        d = dict(zip(range(26), strs))

        ans = list()

        while columnNumber:
            columnNumber -= 1
            temp = columnNumber % 26
            ans.insert(0, d[temp])
            columnNumber = columnNumber // 26

        return ''.join(ans)
