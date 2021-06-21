#!/usr/bin/python3

"""
方法二：二进制枚举
另一种枚举方法是枚举所有 2^{10}=1024 种灯的开闭组合，即用一个二进制数表示灯的开闭，其高 44 位为小时，低 66 位为分钟。
若小时和分钟的值均在合法范围内，且二进制中 11 的个数为 turnedOn，则将其加入到答案中。

"""

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()

        for i in range(1024):
            h, m = i >> 6, i & 0x3f
            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                ans.append(f"{h}:{m:02d}")

        return ans
