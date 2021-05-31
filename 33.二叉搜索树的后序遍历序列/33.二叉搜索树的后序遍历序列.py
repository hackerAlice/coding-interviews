#!/usr/bin/python3

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder == []: return True
        n = len(postorder)
        for i in range(n):
            if postorder[i] > postorder[-1]:
                break
        left_tree = postorder[:i]
        right_tree = postorder[i:n - 1]

        for num in right_tree:
            if num < postorder[-1]:
                return False
        return self.verifyPostorder(left_tree) and self.verifyPostorder(right_tree)

