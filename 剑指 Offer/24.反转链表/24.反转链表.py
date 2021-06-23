#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        result = None

        node = head
        while node:
            if not result:
                result = ListNode(node.val)
            else:
                temp = ListNode(node.val)
                temp.next = result
                result = temp
            node = node.next

        return result