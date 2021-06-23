#!/usr/bin/python3

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        first = None
        second = None

        while head:
            if not first:
                first = ListNode(head.val)
                second = first
            else:
                if head.val < x:
                    node = ListNode(head.val)
                    node.next = first
                    first = node
                else:
                    node = ListNode(head.val)
                    second.next = node
                    second = node
            head = head.next

        return first
