#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        low, high = 0, len(nums) - 1
        middle = (low + high) // 2

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[low:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])

        return root