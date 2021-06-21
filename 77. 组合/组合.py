#!/usr/bin/python3

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backstack(nums):
            if len(path) == k:
                ans.append(list(path))
                return

            for i in range(len(nums)):
                path.append(nums[i]+1)
                backstack(nums[i+1:])
                path.pop()

        path = []
        ans = []
        backstack(list(range(n)))

        return ans


if __name__ == "__main__":
    print(Solution().combine(3, 3))