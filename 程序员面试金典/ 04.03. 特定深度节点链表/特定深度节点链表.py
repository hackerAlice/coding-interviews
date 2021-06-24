#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []

        q = list((tree,))
        ans = list()

        while q:
            head = None
            list_node = None
            for _ in range(len(q)):
                tree_node = q.pop(0)
                if not head:
                    head = ListNode(tree_node.val)
                    list_node = head
                else:
                    list_node.next = ListNode(tree_node.val)
                    list_node = list_node.next

                if tree_node.left:
                    q.append(tree_node.left)

                if tree_node.right:
                    q.append(tree_node.right)

            ans.append(head)

        return ans
