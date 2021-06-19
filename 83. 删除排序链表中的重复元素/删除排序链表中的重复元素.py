#!/usr/bin/python3

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = head
        while first and first.next:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next

        return head