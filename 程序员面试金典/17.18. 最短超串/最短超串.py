#!/usr/bin/python3

from typing import List
import collections


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        def contains(a, b):
            if len(a) < len(b): return False
            for c in b:
                if a[c] < b[c]:
                    return False
            return True
        t = collections.Counter(small)
        dic = collections.defaultdict(int)
        left, right = 0, 0
        res = []
        while right < len(big):
            dic[big[right]] += 1
            while contains(dic, t):
                if not res or right - left < res[1] - res[0]:
                    res = [left, right]
                dic[big[left]] -= 1
                left += 1
            right += 1
        return res
