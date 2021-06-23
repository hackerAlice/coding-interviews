#!/usr/bin/python3

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1

        while low < high:
            middle = (high + low) // 2
            if numbers[middle] > numbers[high]:
                low = middle + 1
            elif numbers[middle] < numbers[high]:
                high = middle
            else:
                high = high - 1

        return numbers[low]
