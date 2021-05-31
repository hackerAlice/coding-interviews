#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)

        node1 = l1
        node2 = l2
        node3 = result

        while node1 and node2:
            if node1.val <= node2.val:
                node3.next = ListNode(node1.val)
                node1 = node1.next
            else:
                node3.next = ListNode(node2.val)
                node2 = node2.next
            node3 = node3.next

        while node1:
            node3.next = ListNode(node1.val)
            node1 = node1.next
            node3 = node3.next

        while node2:
            node3.next = ListNode(node2.val)
            node2 = node2.next
            node3 = node3.next

        return result.next
