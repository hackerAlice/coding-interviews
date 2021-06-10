#!/usr/bin/python3

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first, last = 0, len(nums) - 1
        while first < last:
            if nums[first] + nums[last] > target:
                last -= 1
            elif nums[first] + nums[last] < target:
                first += 1
            else:
                return list((nums[first], nums[last]))

        return []