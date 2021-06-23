from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        d = dict()

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        if target in d:
            return d[target]
        else:
            return 0