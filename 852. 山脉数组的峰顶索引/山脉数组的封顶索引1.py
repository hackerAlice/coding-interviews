#!/usr/bin/python3

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i]> arr[i-1]:
                i += 1
            else:
                return i-1
