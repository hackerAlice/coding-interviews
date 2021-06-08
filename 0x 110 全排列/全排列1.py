"""
使用深度优先算法
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ret = []

        def dfs(li):
            if len(li) == len(path):
                ret.append(path[:])

            for i in li:
                if i not in path:
                    path.append(i)
                    dfs(li)
                    path.pop()

        dfs(nums)
        return ret
