#!/usr/bin/python3
"""
利用最小堆来做
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n-1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if (cur * factor) not in seen:
                     seen.add(cur * factor)
                     heapq.heappush(heap, cur*factor)
        return heapq.heappop(heap)